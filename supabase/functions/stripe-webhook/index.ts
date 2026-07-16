// supabase/functions/stripe-webhook/index.ts
// Stripe webhook — fires on checkout.session.completed.
// Generates a JAI- license key, stores it, and emails it to the buyer via Resend.
//
// Deploy:  supabase functions deploy stripe-webhook --no-verify-jwt
// Secrets: STRIPE_WEBHOOK_SECRET, RESEND_API_KEY, RESEND_FROM (optional)
//
// Each Stripe Payment Link must set metadata: product = <slug below>.

import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const STRIPE_WEBHOOK_SECRET = Deno.env.get("STRIPE_WEBHOOK_SECRET")!;
const RESEND_API_KEY = Deno.env.get("RESEND_API_KEY")!;
const RESEND_FROM = Deno.env.get("RESEND_FROM") || "Jeong AI <info@jeongai.com>";
const REPLY_TO = Deno.env.get("RESEND_REPLY_TO") || "derrick@jeongai.com";

const PRODUCTS: Record<string, { name: string; accessUrl: string }> = {
  "ai-starter-kit": {
    name: "AI Starter Kit",
    accessUrl: "https://www.jeongai.com/starter-kit.html",
  },
  "automation-blueprint": {
    name: "Automation Blueprint",
    accessUrl: "https://www.jeongai.com/files/blueprint.html",
  },
  "automation-toolkit": {
    name: "Automation Toolkit",
    accessUrl: "https://www.jeongai.com/files/toolkit.html",
  },
};

serve(async (req) => {
  const signature = req.headers.get("stripe-signature");
  const body = await req.text();

  if (!(await verifyStripeSignature(body, signature, STRIPE_WEBHOOK_SECRET))) {
    return new Response("Unauthorized", { status: 401 });
  }

  const event = JSON.parse(body);
  if (event.type !== "checkout.session.completed") {
    return new Response("Ignored", { status: 200 });
  }

  const session = event.data?.object;
  if (!session || session.payment_status !== "paid") {
    return new Response("Not paid", { status: 200 });
  }

  const email = session.customer_details?.email || null;
  const name = session.customer_details?.name || null;
  const productSlug = session.metadata?.product || "ai-starter-kit";
  const product = PRODUCTS[productSlug] || PRODUCTS["ai-starter-kit"];

  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
  );

  // Idempotency: Stripe retries webhooks — reuse the key if this session was processed
  const { data: existing } = await supabase
    .from("license_keys")
    .select("key")
    .eq("order_id", session.id)
    .maybeSingle();

  let licenseKey = existing?.key;

  if (!licenseKey) {
    licenseKey = generateKey();
    const { error } = await supabase.from("license_keys").insert({
      key: licenseKey,
      order_id: session.id,
      customer_email: email,
      customer_name: name,
      product: productSlug,
    });
    if (error) {
      console.error("DB insert failed:", error);
      return new Response("DB error", { status: 500 });
    }
  }

  if (email) {
    const sent = await sendKeyEmail(email, name, licenseKey, product);
    if (!sent) {
      // Key exists in DB; admin can resend manually. Return 500 so Stripe retries.
      console.error(`Email failed for ${email} (key ${licenseKey})`);
      return new Response("Email error", { status: 500 });
    }
  } else {
    console.error(`No email on session ${session.id} (key ${licenseKey})`);
  }

  console.log(`Key ${existing ? "resent" : "created"}: ${licenseKey} for ${email} (${productSlug})`);
  return new Response(JSON.stringify({ ok: true }), {
    headers: { "Content-Type": "application/json" },
    status: 200,
  });
});

function generateKey(): string {
  const chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; // no ambiguous chars (0/O, 1/I)
  const bytes = new Uint8Array(12);
  crypto.getRandomValues(bytes);
  const pick = (b: number) => chars[b % chars.length];
  const s = Array.from(bytes, pick).join("");
  return `JAI-${s.slice(0, 4)}-${s.slice(4, 8)}-${s.slice(8, 12)}`;
}

async function sendKeyEmail(
  to: string,
  name: string | null,
  key: string,
  product: { name: string; accessUrl: string },
): Promise<boolean> {
  const firstName = name ? name.split(" ")[0] : "there";
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: RESEND_FROM,
      // Interim: info@ mailbox doesn't exist yet — route replies to derrick@
      reply_to: REPLY_TO,
      to: [to],
      subject: `Your ${product.name} license key`,
      html: `
        <div style="font-family:Arial,Helvetica,sans-serif;max-width:560px;margin:0 auto;color:#1a2b3c;">
          <h2 style="color:#083d6b;">Thanks for your purchase, ${escapeHtml(firstName)}!</h2>
          <p>Here is your license key for the <strong>${product.name}</strong>:</p>
          <p style="background:#f4f6f8;border:1px solid #d9e0e7;border-radius:6px;padding:16px;
                    font-family:Consolas,Menlo,monospace;font-size:18px;letter-spacing:1px;text-align:center;">
            ${key}
          </p>
          <p>Access your content here:<br>
            <a href="${product.accessUrl}" style="color:#c7553b;">${product.accessUrl}</a>
          </p>
          <p>Save this email — you'll need the key whenever you unlock the content on a new device.</p>
          <p style="color:#6b7a89;font-size:13px;margin-top:32px;">
            Questions? Just reply to this email.<br>
            Jeong AI — a division of EBYG Media LLC
          </p>
        </div>
      `,
    }),
  });
  if (!res.ok) {
    console.error("Resend error:", res.status, await res.text());
    return false;
  }
  return true;
}

function escapeHtml(s: string): string {
  return s.replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!
  );
}

// Stripe signature: "t=<ts>,v1=<hex hmac sha256 of `${ts}.${body}`>"
async function verifyStripeSignature(
  body: string,
  header: string | null,
  secret: string,
): Promise<boolean> {
  if (!header) return false;
  try {
    const parts = Object.fromEntries(
      header.split(",").map((kv) => kv.split("=") as [string, string]),
    );
    const timestamp = parts["t"];
    const expected = parts["v1"];
    if (!timestamp || !expected) return false;

    // Reject stale events (5 min tolerance) to limit replay
    if (Math.abs(Date.now() / 1000 - Number(timestamp)) > 300) return false;

    const key = await crypto.subtle.importKey(
      "raw",
      new TextEncoder().encode(secret),
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"],
    );
    const sig = await crypto.subtle.sign(
      "HMAC",
      key,
      new TextEncoder().encode(`${timestamp}.${body}`),
    );
    const computed = Array.from(new Uint8Array(sig))
      .map((b) => b.toString(16).padStart(2, "0"))
      .join("");
    return timingSafeEqual(computed, expected);
  } catch {
    return false;
  }
}

function timingSafeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}
