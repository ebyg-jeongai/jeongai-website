# Critique: jeongai.com rebuild, round 1

Rendered with `hooks/craft/render.js` at 390 by 844 and 1440 by 900, fold and full, for:
home, checkout-starter-kit, purchase-success, starter-kit (unlock screen), starter-kit-demo,
privacy. Captures in `.craft/shots/<page>/`. vault-login uses root-absolute asset paths so
it cannot render from a file URL; it is verified by reading the markup and on staging.

## Findings and fixes

| # | Page | Finding | Fix | Status |
|---|---|---|---|---|
| 1 | Home | Gold mark was a broken image. The repo's brand folder never held the guideline gold and ink marks. | Copied `jeong-mark-gold.png` and `jeong-mark-ink.png` from the approved demo into `brand/assets/`. | Fixed |
| 2 | Product apps | Unlock screens showed a lightning-bolt icon in a blue square as the logo. Not the brand mark, and an icon. | Replaced with the small gold brushed mark on both apps. CSS added to kit.css and blueprint.css. | Fixed |
| 3 | Product apps | Upgrade panel copy promised "white-label assets and ongoing support", which the Toolkit does not include, and used "next-level". | Rewritten to the Toolkit's published contents. | Fixed |
| 4 | Blueprint app | "Best Value" badge on the upgrade card. | Removed. | Fixed |
| 5 | Blueprint app | Check-mark glyphs as list markers in the unlock includes grid. | Glyphs removed; a hairline dash is drawn by CSS instead. | Fixed |
| 6 | Apps and demo | Em-dashes throughout visible copy, as HTML entities the lint did not catch. | Entities replaced with commas mechanically. The ban-list rule now also matches `&mdash;` and numeric entities. | Fixed |
| 7 | Apps and demo | Sidebar section label read "Get started". | Renamed "Setup". | Fixed |
| 8 | Demo | Inline styles still named Montserrat for locked-card labels. | Switched to the sans token. | Fixed |
| 9 | Stylesheets | kit.css, blueprint.css, vault.css and admin.css carried a purple family, greens, ambers, white cards, 12 px radii and shadows. | Mechanical remap: every hex to the nearest brand token, radii above 2 px flattened, shadows removed. Structure untouched. | Fixed |

## Checklist, round 1

1. Specificity. Logo hidden, every public page is recognisable from the type, palette and 정 dictionary entry. Checkout pages carry the same rhythm and published prices. Pass.
2. Hierarchy. One focal point per screen. Title blocks on navy give the product name and price the first two positions. Pass.
3. Typography. Cormorant 300 and 400, Inter 400 and 500, one ladder via tokens across every stylesheet. Pass.
4. Spacing. Eight-step scale, hairlines instead of cards. Pass.
5. Colour. Brand palette only. No gradients, purple, terracotta. Muted red for errors only. Pass.
6. Imagery. Marks only, within clear space. No photography or stock. Pass.
7. Voice. Brand lines verbatim. Live copy reused with em-dashes removed. Buttons name the action and price. Founder quote edits listed in decisions.md under Voice. Pass.
8. Interaction. Phone number on every masthead. One primary action per screen. FAQs open, no accordion. Menu toggles with text, closes on Escape. Pass.
9. Accessibility. Skip link, visible focus, labelled fields, heading outline, reduced motion, 44 px targets. Pass.
10. Sameness audit. Present: a closing purchase section on each checkout page, recorded in the Layout decision as the single call to action. Absent: everything else on the list. Pass.

## Preserved, verified by grep

- GA4 id and the four events. Web3Forms endpoint and access key. Three Stripe Payment Links. Supabase validate-key call, anon key and localStorage keys untouched inside the apps. SWA auth routes. OG and JSON-LD on every public page. llms.txt link. Footer phone on every page.

## Bugs fixed in this branch

- Purchase success and the Stripe webhook now send Blueprint and Toolkit buyers to `automation-blueprint.html`, which validates keys. The Toolkit tier unlocks the Blueprint app per the tier ladder.
- Placeholder Stripe link in the Blueprint upgrade button replaced with the Toolkit link.
- Key hint and placeholder read JAI-XXXX-XXXX-XXXX in both apps; maxlength 19.
- llms.txt tiers and prices match the homepage; the two gated apps removed from its page list; the free demo added.
- sitemap.xml: gated apps removed, free demo added, lastmod refreshed.
- `/proposals/*` removed from the navigation fallback exclude list.

## Moved out of the deploy

`_private/` holds the Precision Trusses estimate, the NexSys proposal, `files/`, the three
generate scripts, `docs/`, and the brand PDF. The workflow deletes `_private`, `supabase`,
`.claude`, `.craft` and `.github` on the runner before upload. `supabase/.temp/` is
gitignored and removed from the index.

## Open items for the owner

- The Supabase webhook source changed but is not deployed. Run `supabase functions deploy stripe-webhook` when ready, or say so and it gets done.
- No Toolkit-only content exists. Toolkit buyers get the Blueprint app until a Toolkit app is built.
- The product apps' interiors (tool cards, prompt library, system builder) keep their own layouts under the new palette. A full pass on those would need its own brief.
- Quote edits to the founder's words are listed in decisions.md under Voice and await confirmation.
- Fonts load from Google Fonts. Self-hosting needs a CSP change (`font-src 'self'`).
- privacy.html and terms.html keep their em-dashes. The brief says the legal text is unchanged, and punctuation edits to legal wording are the owner's call, not a design pass.
- Sidebar icon glyphs in both apps and the demo were removed rather than redrawn. Navigation is text only, per the Components decision.
- The Blueprint app interior still uses a check glyph for completed checklist items and star glyphs for tool ratings. Those carry state, not decoration, so they were left in place. The ban-list lint reports them and will keep doing so until the owner either accepts them in `.craft/ban-list.json` or a later pass redraws them as text.
