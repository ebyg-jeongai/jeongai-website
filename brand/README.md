# Jeong AI — Brand System

A self-contained brand kit for Jeong AI (a division of EBYG Media LLC). All files
share one stylesheet (`brand.css`) so the guidelines and the documents can never
drift apart.

## Files

| File | Purpose |
|------|---------|
| `brand.css` | **Single source of truth.** Brand tokens (color, type, shape) mirrored from the live site's `/css/styles.css`, plus the print-ready document shell. |
| `brand-guidelines.html` | Visual brand reference — logo, palette, type, voice. Open in a browser; prints to PDF. |
| `invoice.html` | Repeatable invoice. Click-to-edit fields, "+ Add line item", Print → Save as PDF. |
| `proposal.html` | Repeatable proposal — cover, scope, tiered pricing, timeline, signature block. |
| `logo-explorations.html` | The full lockup sheet — every approved lockup and its role. |
| `assets/` | Logo source files (see below). |

## Logo system

The identity is the **정 brush mark** (Korean for "Jeong," hand-lettered) + the
Montserrat **"Jeong AI"** wordmark. Approved lockups and their roles:

| Lockup | Role |
|--------|------|
| Horizontal (mark left of wordmark) | **Primary** — site header, email signature, letterhead |
| Formal (mark + rule + endorsement) | Documents — invoices, proposals, contracts |
| Stacked (mark above wordmark) | Square spaces — business cards, slide titles |
| Reversed (white mark on blue/ink) | Dark backgrounds, proposal covers, social headers |
| Seal tile (mark in rounded blue square) | Favicon, app icon, social avatar |

**Rule of thumb:** mark color follows the background — `jeong-mark-ink` / `-blue` on
light, `jeong-mark-white` on dark. Never the dark mark on a dark field.

### Assets

| File | Use |
|------|-----|
| `jeong-mark-original.png` | Untouched source (transparent, 2508²). |
| `jeong-mark-ink.png` / `-blue.png` / `-terracotta.png` | Recolored marks for light backgrounds. |
| `jeong-mark-white.png` | Mark for dark backgrounds. |
| `icon-512.png` / `apple-touch-icon.png` (180) / `favicon-32.png` | App/favicon tiles (white mark on Jeong Blue). |

The mark is kept as **high-resolution PNG**, not SVG — vector-tracing a brush stroke
flattens its calligraphic texture. The 2508px source scales cleanly for print.

## How to create an invoice or proposal

1. Open `invoice.html` (or `proposal.html`) in a browser.
2. Click any field and type — every editable value is highlighted on hover.
3. Use **+ Add line item** (invoice) to extend the table.
4. Click **Print / Save PDF** → choose "Save as PDF", **US Letter**, margins *Default*.
   - Tip: turn **off** "Headers and footers" in the print dialog for a clean page.

Nothing is saved automatically — these are stateless templates. Save the PDF, or
duplicate the HTML file if you want a stored copy of a specific document.

## Brand quick reference

- **Wordmark:** "Jeong" (Montserrat 700, `#0A4F8A`) + "AI" (Montserrat 500, `#6B6B7B`). Text only — no image logo.
- **Primary blue** `#0A4F8A` · **Terracotta accent** `#C7553B` · **Ink** `#1A1A2E`
- **Type:** Montserrat (headings) / Source Sans 3 (body)
- **Contact:** (801) 648-9652 · info@jeongai.com · jeongai.com
- **Tagline:** *Consistent presence. Genuine care. Quiet reliability.*

## Note on legacy branding

The repo's `generate_letterhead.py` uses retired **"EBYG Automation"** branding
(navy/gold, `ebygautomation.com`). That is superseded by this kit — always use the
Jeong AI details above. Per `CLAUDE.md`, Jeong AI / jeongai.com is canonical.

To keep this kit in sync with the site: if a color or font changes in
`/css/styles.css`, update the matching token in `brand.css` and everything follows.
