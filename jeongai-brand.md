# Jeong AI — Brand & Design Reference

Use this document to maintain visual and tonal consistency across all content, designs, and AI-generated materials for Jeong AI.

---

## Identity

| Field | Value |
|---|---|
| **Brand name** | Jeong AI |
| **Parent company** | EBYG Media LLC |
| **Tagline** | Software Is Not One Size Fits All |
| **Page title format** | `Jeong AI — Custom Software & AI Tools Built for Your Business` |
| **Meta description** | Software is not one size fits all. Custom software, AI agents, and automated workflows built precisely around how your business works. |
| **Domain** | jeongai.com |
| **Phone** | (801) 648-9652 |
| **Email** | info@jeongai.com |

---

## Logo

The logo is **text-only** — no image file. It renders as two adjacent spans:

```
"Jeong"  → Montserrat Bold, primary blue (#0a4f8a)
"AI"     → Montserrat Medium (500), muted text (#6b6b7b)
```

- Font size: 1.6rem / 1.1rem
- Gap between words: 0.35rem
- No icon, no symbol, no wordmark image

The Korean character **정 (jeong)** is used as a decorative brand symbol in certain UI contexts (large display card). It carries meaning around warmth, care, and relationship — central to the brand philosophy.

---

## Color Palette

### Primary Colors

| Name | Hex | CSS Variable | Primary Usage |
|---|---|---|---|
| Primary Blue | `#0a4f8a` | `--primary` | Buttons, links, icons, borders, headings |
| Primary Dark | `#083d6b` | `--primary-dark` | Gradient ends, hover states |
| Primary Light | `#1a6fb8` | `--primary-light` | Emphasis text on dark backgrounds |

### Accent Colors

| Name | Hex | CSS Variable | Primary Usage |
|---|---|---|---|
| Accent Red-Orange | `#c7553b` | `--accent` | CTA buttons, pricing, badges, hover highlight |
| Accent Hover | `#a8432d` | `--accent-hover` | Hover state on accent elements |

### Neutral / Background Colors

| Name | Hex | CSS Variable | Primary Usage |
|---|---|---|---|
| Dark Navy | `#1a1a2e` | `--dark` | Footer, dark sections, heading color |
| Body Text | `#3a3a4a` | `--text` | All body copy |
| Light Text | `#6b6b7b` | `--text-light` | Secondary text, captions, descriptions |
| Light Background | `#f7f8fa` | `--light` | Section backgrounds (alternating) |
| Warm Background | `#f2ede3` | *(inline)* | Conviction/quote sections |
| White | `#ffffff` | `--white` | Cards, page background, text on dark |
| Border | `#e2e4e8` | `--border` | Card borders, dividers, input borders |

### Extended Palette (available, rarely used on main site)

| Name | Hex | CSS Variable |
|---|---|---|
| Purple | `#7C3AED` | `--purple` |
| Purple Mid | `#8B5CF6` | `--purple-mid` |
| Purple Light | `#EDE9FE` | `--purple-light` |
| Purple Pale | `#F5F3FF` | `--purple-pale` |

---

## Typography

### Fonts

| Role | Family | Weights | Source |
|---|---|---|---|
| Headings | Montserrat | 400, 500, 600, 700 | Google Fonts |
| Body | Source Sans 3 / Source Sans Pro | 300, 400, 500, 600 | Google Fonts |

### Type Scale

| Element | Size | Weight | Color |
|---|---|---|---|
| h1 | 3.2rem (→ 2.6 → 2.2 → 1.9rem responsive) | 600 | `--dark` |
| h2 | 2.4rem (→ 2.0 → 1.75 → 1.5rem) | 600 | `--dark` |
| h3 | 1.4rem | 600 | `--dark` |
| h4 | 1.1rem | 600 | `--dark` |
| Body base | 17px / 1.65 line-height | 400 | `--text` |
| Lead text | 1.15rem / 1.7 line-height | 400 | `--text-light` |
| Section tag | 0.8rem, uppercase, 2px letter-spacing | 600 | `--primary` |
| Small / meta | 0.85–0.93rem | 400–500 | `--text-light` |

---

## Gradients

| Name | Value | Usage |
|---|---|---|
| Primary gradient | `linear-gradient(135deg, #0a4f8a 0%, #083d6b 100%)` | Feature cards, support card, brand card |
| Hero background | `linear-gradient(135deg, #f0f4f8 0%, #e8edf4 40%, #dce4ef 100%)` | Homepage hero section |

---

## Spacing & Layout

| Token | Value |
|---|---|
| Max content width | 1200px |
| Header height | 80px |
| Container padding | 0 2rem (0 1.25rem on mobile) |
| Section padding | 6rem 0 (reduced to 4–3rem on mobile) |
| Border radius (sm) | 6px |
| Border radius (lg) | 12px |
| Transition | 0.25s ease |

---

## Shadows

| Name | Value |
|---|---|
| `--shadow-sm` | `0 1px 3px rgba(0,0,0,0.06)` |
| `--shadow-md` | `0 4px 16px rgba(0,0,0,0.08)` |
| `--shadow-lg` | `0 8px 32px rgba(0,0,0,0.12)` |
| `--shadow-xl` | `0 16px 48px rgba(0,0,0,0.14)` |

---

## Buttons

| Variant | Background | Text | Border | Hover |
|---|---|---|---|---|
| Primary | `#0a4f8a` | white | `#0a4f8a` | bg/border → `#c7553b` |
| Outline | transparent | `#0a4f8a` | `#0a4f8a` | bg → `#0a4f8a`, text → white |
| On dark | transparent | rgba(255,255,255,0.8) | rgba(255,255,255,0.3) | bg → `#0a4f8a` |

- Padding: `0.85rem 2rem` (sm: `0.65rem 1.5rem`)
- Font: Montserrat 600, 0.95rem
- Border radius: 6px

---

## Brand Voice & Tone

- **Direct and confident** — no fluff, no buzzword soup
- **Business-first** — outcomes over features
- **Warm but professional** — not cold, not casual
- **Specific** — "built for your business, not the other ten thousand"
- Avoid: generic SaaS language, hype, vague AI promises

### Key Phrases (reuse these)
- "Software is not one size fits all"
- "Built around how your business actually works"
- "Your systems, not ours"
- "정 (jeong)" — warmth, care, genuine relationship

---

## Two-Brand Structure

Jeong AI operates two related brands under the same umbrella:

| Brand | Focus | Audience |
|---|---|---|
| **Jeong AI** (automation/software) | Custom software, AI agents, automated workflows | Business owners needing custom solutions |
| **Jeong AI** (education/partnership) | AI education, learning programs | Individuals learning AI skills |

The education side graduates into the partnership/services side — it's a pipeline, not two separate companies.

---

## Contact (canonical)

```
Business:  Jeong AI (a division of EBYG Media LLC)
Phone:     (801) 648-9652
Email:     info@jeongai.com
Website:   jeongai.com
Address:   Fully remote — no physical address displayed
Social:    None currently
```
