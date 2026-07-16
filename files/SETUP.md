# EBYG AI Starter Kit — Technical Setup Guide

## What you're deploying

| File | Purpose |
|---|---|
| `kit.html` | The buyer-facing kit app with unlock screen |
| `admin.html` | Your private monitoring dashboard |
| `supabase/schema.sql` | Database tables — run once in Supabase |
| `supabase/functions/validate-key/index.ts` | Validates keys + logs sessions |
| `supabase/functions/stripe-webhook/index.ts` | Creates a key on every Stripe purchase and emails it via Resend |

---

## Step 1 — Supabase setup (15 minutes)

1. Create a free account at **supabase.com**
2. Create a new project (any name, remember the database password)
3. Go to **SQL Editor** → paste and run the contents of `schema.sql`
4. Go to **Settings → API** and copy:
   - Project URL (looks like `https://abcdef.supabase.co`)
   - `anon` public key
   - `service_role` secret key (keep this private)

---

## Step 2 — Deploy Edge Functions (10 minutes)

Install the Supabase CLI:
```bash
npm install -g supabase
supabase login
supabase link --project-ref YOUR_PROJECT_REF
```

Set environment variables:
```bash
supabase secrets set STRIPE_WEBHOOK_SECRET=whsec_...      # from Stripe webhook endpoint
supabase secrets set RESEND_API_KEY=re_...                # from resend.com
supabase secrets set RESEND_FROM="Jeong AI <info@jeongai.com>"  # optional, this is the default
```
(`SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` are provided automatically to edge functions.)

Deploy both functions:
```bash
supabase functions deploy validate-key
supabase functions deploy stripe-webhook --no-verify-jwt
```

Your function URLs will be:
- `https://YOUR_PROJECT.supabase.co/functions/v1/validate-key`
- `https://YOUR_PROJECT.supabase.co/functions/v1/stripe-webhook`

---

## Step 3 — Configure kit.html (5 minutes)

Open `kit.html` and replace these two lines near the top of the `<script>` block:

```javascript
const SUPABASE_URL = 'https://YOUR_PROJECT.supabase.co';
const SUPABASE_ANON_KEY = 'YOUR_ANON_KEY';  // the anon key, NOT service_role
```

---

## Step 4 — Configure admin.html (2 minutes)

Open `admin.html` and change the admin password:

```javascript
const ADMIN_PASSWORD = 'jai-admin-2024'; // Change this to something strong
```

The Supabase URL and service role key are entered at login — no hardcoding needed.

---

## Step 5 — Set up Stripe (15 minutes)

1. In the Stripe Dashboard, create one **Product** per offering (Starter Kit, Blueprint, Toolkit) with a one-time price.
2. Create a **Payment Link** for each product. On each link, set **Metadata**:
   - key: `product`
   - value: `ai-starter-kit`, `automation-blueprint`, or `automation-toolkit`
3. Set each link's confirmation message to something like:
   > "Your license key is on its way to your email. Save it — you'll need it to unlock your content."
4. Go to **Developers → Webhooks → Add endpoint**:
   - **URL:** `https://YOUR_PROJECT.supabase.co/functions/v1/stripe-webhook`
   - **Events:** `checkout.session.completed`
   - Copy the **Signing secret** → set it as `STRIPE_WEBHOOK_SECRET` above
5. Paste each Payment Link URL into the matching checkout page (`checkout-*.html`), replacing the `https://buy.stripe.com/REPLACE_WITH_..._LINK` placeholders.

Now every purchase automatically creates a key and emails it to the buyer.

**Tier enforcement:** keys unlock their own tier and everything below it
(`automation-toolkit` ⊇ `automation-blueprint` ⊇ `ai-starter-kit`). The unlock
pages send their product slug to `validate-key`, which compares it against the
`product` column on the key. A Starter Kit key will not unlock the Blueprint
or Toolkit pages.

---

## Step 6 — Set up Resend (10 minutes)

1. Create a free account at **resend.com**
2. Add and verify the `jeongai.com` domain (DNS records shown in their dashboard)
3. Create an API key → set it as `RESEND_API_KEY` above

The webhook sends the license key from `Jeong AI <info@jeongai.com>` with a link to the content.

---

## Step 7 — Deploy the files

**Option A — Host kit.html on your existing site (recommended)**

Upload `kit.html` to your web host as `/kit/index.html`
→ Accessible at `kit.jeongai.com` (set up a subdomain in DNS)

Upload `admin.html` somewhere private — a `/admin` path with HTTP basic auth, or just open it locally.

**Option B — Netlify (free)**

Drag both HTML files into a new Netlify site. Set up a custom domain for the kit.

---

## Step 8 — Test end-to-end

1. Insert a test key manually in Supabase:
   ```sql
   INSERT INTO license_keys (key, customer_email, notes)
   VALUES ('JAI-TEST-0000-0001', 'you@youremail.com', 'Test key');
   ```
2. Open `kit.html` → enter `JAI-TEST-0000-0001` → should unlock
3. Check `admin.html` → the session should appear in the table

---

## Monitoring thresholds

The system flags any key with **20+ sessions in 30 days** as unusual. You can adjust this:

In `supabase/functions/validate-key/index.ts`:
```typescript
const ALERT_THRESHOLD = 20; // Change this number
```

A "device" is tracked by browser fingerprint (non-reversible hash of user agent + screen + timezone). One person using the kit on their laptop + phone = 2 devices. Anything over 4–5 unique devices on a single key is worth a look.

---

## Questions

hello@jeongai.com
