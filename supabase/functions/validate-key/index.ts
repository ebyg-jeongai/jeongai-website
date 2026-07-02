import { serve } from "https://deno.land/std@0.168.0/http/server.ts";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

serve(async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  try {
    const { key, fingerprint } = await req.json();

    if (!key || key.length < 10) {
      return new Response(
        JSON.stringify({ valid: false, reason: "Invalid key" }),
        { headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    // Call Lemon Squeezy License API — no API key required, this endpoint is public
    const lsRes = await fetch("https://api.lemonsqueezy.com/v1/licenses/activate", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        license_key: key,
        instance_name: fingerprint || "browser",
      }).toString(),
    });

    const lsData = await lsRes.json();

    if (lsData.activated) {
      return new Response(
        JSON.stringify({ valid: true }),
        { headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    // If this device already activated this key, LS returns an error but the key is still valid
    const error = (lsData.error || "").toLowerCase();
    if (error.includes("already") || error.includes("instance")) {
      return new Response(
        JSON.stringify({ valid: true }),
        { headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    return new Response(
      JSON.stringify({ valid: false, reason: lsData.error || "Invalid license key" }),
      { headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  } catch (_err) {
    return new Response(
      JSON.stringify({ valid: false, reason: "Validation service unavailable" }),
      { headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  }
});
