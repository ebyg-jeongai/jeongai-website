# Design decisions: jeongai.com rebuild

<!--
The seven demo decisions carry over unchanged in substance. They are restated here so this
file is complete on its own, then extended for a multi-page site with live commerce.
Sources: [BG] Brand Guidelines 2026, [REPO] this repository, [DEMO] the approved demo,
[USER] the owner, and the reference library where a book informed a choice.
-->

## Typography

**Area:** Typography
**Default:** Inter or Geist at Tailwind's default scale. The current site uses Montserrat and Source Sans 3, and two other type systems on inner pages.
**Chosen:** Cormorant Garamond for every headline and brand line, 300 and 400, mostly italic, at editorial sizes. Inter for body, navigation, labels, tables and the product apps' interface text, 400 and 500. Eyebrows in uppercase Inter 500 with 0.18em tracking. Noto Serif KR light for typed Hangul. One seven-step type ladder shared by every page through CSS custom properties in css/styles.css. Body measure 60 to 68 characters. The product apps' dense tool and prompt lists use the small end of the ladder in Inter.
**Why this subject:** The guidelines mandate this pairing [BG p.8]. The owner approved it in the demo [USER]. The current repo has three unrelated type systems, which is the opposite of a brand [REPO inventory].
**Swap test:** Fails for any competitor with a sans identity.
**Source:** [BG p.8]; Refactoring UI, type hierarchy; Practical UI, scale and measure.

## Color

**Area:** Color
**Default:** White page, blue accent, terracotta highlight, grey text, card shadows. Purple utility colours in places.
**Chosen:** Navy #111827 dominant, Parchment #F5F1E8 for reading and forms, Primary Blue #0A4F8A for links, buttons on parchment and structural rules, Gold #C9A96E for the mark on navy, eyebrows on navy and one hairline per navy section. Ink #1F2937 body on parchment. Sky Blue unused. No gradients, no terracotta, no purple. The product apps' status colours (valid key, error, badge tints) are re-derived from this palette: blue for information, gold for success, ink for neutral, and a single muted red #8B3A2F only for errors.
**Why this subject:** The guidelines' palette and proportion rule [BG p.7]. The owner chose the PDF as authoritative over the live CSS [USER].
**Swap test:** Not transferable with a brushed ideogram.
**Source:** [BG p.5, p.7]; Inclusive Design, contrast.

## Layout

**Area:** Layout
**Default:** Hero with two buttons, stat strip, feature cards, pricing cards with a Most Popular badge, testimonial strip, call-to-action band.
**Chosen:** The demo's brand-book rhythm on every public page: single column on phones, a 14rem label column plus content column on desktop, surfaces alternating navy and parchment, hairlines instead of cards. Home follows the demo's opening and adds, in this order: four functions as a two-by-two definition grid on parchment; process as a numbered ledger of four; digital products as a plain table with a description column and a link per row; newsletter as one field and one button on navy; implementation tiers as a table with a "Best for" line under each name and no badge; support plan as a short statement block; websites as one paragraph; audit as the closing statement with the form. Checkout pages: title block on navy with the price set large in Cormorant, then on parchment a "What's included" ledger, the Stripe button, and every FAQ open as a definition list. Success page: one navy statement, the unlock link as the single button. Legal pages: parchment, one column, the existing text with the type ladder applied. Vault login: navy, wordmark, three plain links.
**Why this subject:** The owner approved the rhythm on the demo [USER]. Prices are published in full, which is true here and nowhere else in the category, so they are set as tables, the form for comparable data, rather than as competing cards [REPO, brief]. No testimonials exist, so no strip [brief]. Accordions hide the FAQs the inventory judged the most useful copy on the checkout pages; open lists respect that [REPO inventory].
**Swap test:** A dictionary entry for 정, a founder quote, published cumulative pricing and an open FAQ set cannot move to a competitor intact.
**Source:** [USER]; Designing Interfaces, tables and page layout patterns; Laws of UX, Hick's law.

## Imagery

**Area:** Imagery
**Default:** Stock photos or isometric illustrations.
**Chosen:** No photographs. The brushed 정 in gold on navy on the home opening screen and as the headword of the dictionary entry in ink. On inner pages, the mark appears once, small, in the masthead lockup only. The product apps show no mark beyond the masthead. Guideline clear-space and minimum-size rules obeyed everywhere.
**Why this subject:** No imagery exists and the owner said the mark carries it [USER]. The guidelines say the texture is the point [BG p.3].
**Swap test:** Fails; the mark is the identity.
**Source:** [BG p.3, p.6]; [USER].

## Voice

**Area:** Voice
**Default:** Marketing register, filler superlatives, paraphrased quotes.
**Chosen:** The guideline voice exactly [BG p.9]. Existing copy reused verbatim where it already meets the voice; em-dashes replaced with periods and commas. Buttons name the action: "Book a free automation audit", "Buy the Starter Kit, $29", "Enter your key". The site says plainly: one person, northern Utah, since 2025.
**Why this subject:** [BG p.9]; the owner's words are the strongest copy available [USER].
**Swap test:** The brand lines and the founder's quote are untransferable.
**Quote edits:** Two edits carried from the demo, pending the owner's confirmation. Original "charm" set as "jeong" (the owner was describing 정). Original "more powerful" set as "more capable" to fit the guideline voice. Original "how your software solutions work for you" set as "how your software works for you". If the owner prefers the originals, they are restored verbatim.
**Source:** [BG p.9]; [USER].

## Components

**Area:** Components
**Default:** Cards with shadows and 12 px radii, icon sets, accordions, badges, scroll-reveal animation.
**Chosen:** No framework, no icons, no cards, no badges, no accordions. Hairline rules, one button style per surface (parchment fill on navy, navy fill on parchment, 2 px radius, no shadow), underlined links, plain tables with tabular numerals, definition lists. Forms: fields as underlined inputs on parchment with Inter labels above, one button, no placeholder text as label, visible focus. Motion: one opacity fade on the home mark; the scroll-reveal system and its selectors are removed from main.js. The product apps keep their interactive components (key gate, filters, drag-and-drop builder) but their containers become hairline-ruled blocks in the palette, without shadows or radii above 2 px.
**Why this subject:** The owner chose plain HTML and CSS [USER]. The guidelines forbid effects around the mark and describe the brand as calm and unhurried [BG p.3, p.6]. Removing the component vocabulary of the template era is the visible proof that someone built this [USER].
**Swap test:** Derived from this palette and mark.
**Source:** [USER]; [BG]; Practical UI, spacing.

## Responsiveness

**Area:** Layout: breakpoints
**Default:** Desktop design squeezed down.
**Chosen:** Designed at 390 px first, one breakpoint at 900 px, clamp() type, 44 px targets. Tables on phones keep two columns at most; a third column, such as a product description, moves under the name.
**Why this subject:** Most visitors on phones [USER].
**Source:** [USER]; Laws of UX, Fitts's law.

## Navigation and page chrome

**Area:** Components: masthead, navigation, footer
**Default:** Logo left, six links, a coloured "Get Started" button right, hamburger icon on phones, footer with four link columns and social icons.
**Chosen:** Masthead on navy: the typeset wordmark "Jeong AI" in Cormorant with "AI" in gold, matching the approved lockup, and on inner pages the small mark before it. Four links: Products, Systems, Websites, Audit, plus the phone number as text. On phones the links collapse behind a text button reading "Menu" that toggles to "Close", using the existing main.js contract, no icon. Footer on navy, one column: the attribution line, phone and email as links, privacy and terms, and the signature close "Always there. That's 정." No social links, per CLAUDE.md.
**Why this subject:** The approved lockup sets "AI" in gold [REPO brand/README.md, Downloads lockups]. The business has no social presence to link and displays no address [REPO CLAUDE.md]. One phone number on every screen is the single action the owner wants reachable [USER].
**Swap test:** The gold "AI" and the Hangul close are this brand's.
**Source:** [REPO]; Designing Interfaces, global navigation patterns.

## Stylesheet architecture and cache

**Area:** Components: CSS files
**Default:** One growing stylesheet per page plus inline token copies.
**Chosen:** css/styles.css is rewritten as the design system: tokens, type ladder, surfaces, chrome, tables, ledgers, forms, buttons. Page files remain and are rewritten to use only the tokens: checkout.css, legal.css, vault.css, admin.css. kit.css and blueprint.css are remapped to the tokens with structural rules kept. Inline token copies in vault-login.html are replaced by a link to styles.css. Every stylesheet link carries ?v=20260917.
**Why this subject:** The inventory found tokens re-declared in six places so a change does not propagate, and a manual cache-busting convention that must be honoured or Azure serves stale CSS for a week [REPO].
**Swap test:** Mechanism is generic; the tokens are not.
**Source:** [REPO CHANGELOG, inventory]; Software Engineering at Google on single sources of truth.
