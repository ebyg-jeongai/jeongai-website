---
name: brandedjeong
description: Create a polished, on-brand Jeong AI document (training guide, how-to, report, SOW, one-pager, proposal-style memo, release notes, etc.) as a print-ready HTML file using the Jeong AI brand package. Trigger when the user says "brandedJeong <document type> for/about <subject>" — e.g. "brandedJeong training document for this project", "brandedJeong onboarding guide for the starter kit", "brandedJeong one-pager about our automation service".
argument-hint: "<document type> for/about <subject>"
allowed-tools: Read, Write, Bash, Glob, Grep
---

# brandedJeong — Branded Document Generator

Produce a professional, on-brand **Jeong AI** document as a print-ready HTML file
(open in a browser → Print → Save as PDF). Documents reuse the shared brand
stylesheet, so they always match the website, invoices, and proposals.

Request format: `brandedjeong <document type> for/about <subject>`
(e.g. *"brandedjeong training document for this project"*).

## What to do

### 1. Locate the brand package
The brand package lives at `brand/` in the ebyg-automation repo:
`brand/brand.css`, `brand/assets/`, and reference pages. If you're not sure where
it is, find it: `Glob` for `**/brand/brand.css`. Generated documents go in
`brand/documents/` (create the folder if it doesn't exist) so their relative links
`../brand.css` and `../assets/...` resolve. **Never copy brand values into the new
file** — always link `../brand.css` and use its classes/CSS variables. That keeps
one source of truth.

If no brand package exists in the working tree, tell the user and stop — this skill
depends on it.

### 2. Understand the request
Determine two things:
- **Document type** (training doc, how-to guide, onboarding guide, report, SOW,
  one-pager, memo, release notes, FAQ…). This drives structure (see recipes below).
- **Subject** — what it's about.
  - If the subject is **"this project"** or names something in the codebase, gather
    real content: read `README.md`, `CLAUDE.md`, `CHANGELOG.md`, key source files,
    and relevant HTML/JS. Write accurate, specific content — never invent features.
  - If the subject is external or thin, draft strong placeholder content and clearly
    mark assumptions, or ask 1–2 focused questions if essential facts are missing.

### 3. Build the document
1. Copy `.claude/skills/brandedjeong/template.html` to
   `brand/documents/<slug>.html` (slug = kebab-case of the title).
2. Replace every `{{PLACEHOLDER}}`. Set `{{DOC_TYPE}}` (the kicker, e.g.
   "Training Guide"), `{{DOC_TITLE}}`, `{{DOC_SUBTITLE}}`, `{{DATE}}` (today, long
   form), `{{VERSION}}` (default 1.0).
3. Replace the BODY with real content shaped to the document type. Keep the cover,
   header lockup, footer, and the `../brand.css` link intact.
4. Use the provided brand components for structure (don't hand-roll styles):
   - `<h2><span class="sec-num">01</span>Title</h2>` — numbered section headings
   - `<ol class="steps"><li><span class="step-title">…</span>…</li></ol>` — steps
   - `<div class="callout tip|warn|note"><span class="callout-label">…</span>…</div>`
   - `<table class="doc-table">` — reference tables
   - `<p class="doc-lead">…</p>` — opening summary
   - `<div class="doc-toc">` — table of contents (keep for long docs, remove for short)
   - `<pre><code>…</code></pre>` and inline `<code>` — for technical/software docs
5. Match the brand **voice**: direct, confident, warm, business-first. Short
   sentences, concrete outcomes, no jargon or hype. (See `brand/brand-guidelines.html`
   §06.) Address the reader plainly ("you").
6. Keep section count sensible (3–7 for most docs). Update the TOC to match the real
   sections, or delete it for short documents.

### 4. Deliver
- Open the file in the browser: `start "" brand/documents/<slug>.html` (Windows).
- Tell the user the path and that they can edit any text, then **Print / Save as PDF**
  (US Letter; turn off the browser's headers/footers for a clean page).

## Document-type recipes (structure guidance)

- **Training document / how-to / onboarding** → Lead summary → "What you'll learn"
  → numbered `steps` for the procedure → `callout tip`/`warn` for gotchas →
  "Troubleshooting" or "FAQ" table. Use `<code>`/`<pre>` for software steps.
- **Report / status update** → Executive summary (`doc-lead`) → Findings (sections)
  → Data tables → Recommendations → Next steps.
- **Statement of Work (SOW)** → Overview → Scope (in/out) → Deliverables table →
  Timeline → Investment → Terms. (For pricing-led sales docs, prefer the existing
  `proposal.html` template instead.)
- **One-pager** → Headline value prop → 3 benefit blocks → How it works (steps) →
  Call to action. Drop the TOC.
- **Release notes / changelog** → Version + date → "What's new" (list) → callouts
  for breaking changes → upgrade steps.

## Canonical brand facts (use exactly)
- **Jeong AI**, a division of **EBYG Media LLC**
- (801) 648-9652 · info@jeongai.com · jeongai.com
- Tagline / philosophy: *Consistent presence. Genuine care. Quiet reliability.*
- Logo: the 정 brush mark + Montserrat "Jeong AI" wordmark (already in the template).
- Do **not** use the retired "EBYG Automation" navy/gold branding or the old
  `letterhead` skill — those are superseded by this brand package.
