import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const ALERT_THRESHOLD = 20; // sessions in 30 days before a key is flagged

// Tier hierarchy: a key unlocks its own tier and everything below it.
const TIERS: Record<string, number> = {
  "ai-starter-kit": 1,
  "automation-blueprint": 2,
  "automation-toolkit": 3,
};

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

function json(body: Record<string, unknown>, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...corsHeaders, "Content-Type": "application/json" },
  });
}

async function sha256Hex(input: string): Promise<string> {
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(input));
  return Array.from(new Uint8Array(digest)).map((b) => b.toString(16).padStart(2, "0")).join("");
}

serve(async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  try {
    const { key, fingerprint, ua, product } = await req.json();

    if (typeof key !== "string" || key.trim().length < 10) {
      return json({ valid: false, reason: "Invalid key" });
    }
    const normalizedKey = key.trim().toUpperCase();

    // Which tier is this page asking for? Missing/unknown → lowest tier.
    const requestedTier = TIERS[typeof product === "string" ? product : ""] ?? 1;

    const supabase = createClient(
      Deno.env.get("SUPABASE_URL")!,
      Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    );

    const { data: license, error } = await supabase
      .from("license_keys")
      .select("key, product, revoked, flagged")
      .eq("key", normalizedKey)
      .maybeSingle();

    if (error) {
      console.error("license lookup failed:", error);
      return json({ valid: false, reason: "Validation service unavailable" });
    }
    if (!license) {
      return json({ valid: false, reason: "Invalid license key" });
    }
    if (license.revoked) {
      return json({ valid: false, reason: "This key has been revoked" });
    }

    // Tier enforcement: key must be at or above the tier this page requires
    const keyTier = TIERS[license.product] ?? 1;
    if (keyTier < requestedTier) {
      return json({
        valid: false,
        reason: "Your key doesn't include this product. Upgrade at jeongai.com or contact info@jeongai.com.",
      });
    }

    // Log the session (non-fatal if it fails)
    const ip = req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() || "";
    const { error: sessionError } = await supabase.from("key_sessions").insert({
      key: license.key,
      fingerprint: typeof fingerprint === "string" ? fingerprint.slice(0, 128) : null,
      ip_hash: ip ? await sha256Hex(ip) : null,
      ua: typeof ua === "string" ? ua.slice(0, 120) : null,
    });
    if (sessionError) console.error("session insert failed:", sessionError);

    // Flag unusually heavy usage (non-fatal)
    if (!license.flagged) {
      const since = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString();
      const { count } = await supabase
        .from("key_sessions")
        .select("id", { count: "exact", head: true })
        .eq("key", license.key)
        .gt("accessed_at", since);
      if ((count ?? 0) >= ALERT_THRESHOLD) {
        await supabase
          .from("license_keys")
          .update({ flagged: true, flag_reason: `${count} sessions in 30 days` })
          .eq("key", license.key);
      }
    }

    return json({ valid: true });
  } catch (_err) {
    return json({ valid: false, reason: "Validation service unavailable" });
  }
});
