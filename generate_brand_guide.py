"""Generate JeongAI Brand & Design Reference PDF."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas as pdf_canvas

OUTPUT = "JeongAI_Brand_Guide.pdf"
W, H = letter  # 612 x 792 pts

# ── Colors ────────────────────────────────────────────────────────
PRIMARY       = HexColor("#0a4f8a")
PRIMARY_DARK  = HexColor("#083d6b")
PRIMARY_LIGHT = HexColor("#1a6fb8")
ACCENT        = HexColor("#c7553b")
ACCENT_HOVER  = HexColor("#a8432d")
DARK          = HexColor("#1a1a2e")
TEXT          = HexColor("#3a3a4a")
TEXT_LIGHT    = HexColor("#6b6b7b")
LIGHT         = HexColor("#f7f8fa")
WARM          = HexColor("#f2ede3")
WHITE         = HexColor("#ffffff")
BORDER        = HexColor("#e2e4e8")
MUTED         = HexColor("#aaaaaa")
PURPLE        = HexColor("#7C3AED")
PURPLE_MID    = HexColor("#8B5CF6")
PURPLE_LIGHT  = HexColor("#EDE9FE")
PURPLE_PALE   = HexColor("#F5F3FF")

MG = 0.75 * inch        # margin
HEADER_H = 1.0 * inch
FOOTER_LINE_Y = 0.72 * inch
FOOTER_H = 0.48 * inch
BODY_TOP = H - HEADER_H - 0.28 * inch
BODY_BTM = FOOTER_LINE_Y + 0.08 * inch


# ── Shared helpers ────────────────────────────────────────────────

def header(c, subtitle="Brand & Design Reference"):
    c.setFillColor(DARK)
    c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    c.setStrokeColor(PRIMARY)
    c.setLineWidth(2.5)
    c.line(0, H - HEADER_H, W, H - HEADER_H)

    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 19)
    jw = c.stringWidth("Jeong", "Helvetica-Bold", 19)
    c.drawString(MG, H - 0.55 * inch, "Jeong")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 19)
    c.drawString(MG + jw + 3, H - 0.55 * inch, "AI")

    c.setFillColor(HexColor("#555555"))
    c.setFont("Helvetica", 7)
    c.drawString(MG, H - 0.76 * inch, "A Division of EBYG Media LLC")

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawRightString(W - MG, H - 0.48 * inch, subtitle)
    c.setFillColor(HexColor("#555555"))
    c.setFont("Helvetica", 7)
    c.drawRightString(W - MG, H - 0.68 * inch, "May 2026")


def footer(c, page_num):
    c.setStrokeColor(PRIMARY)
    c.setLineWidth(1.2)
    c.line(MG, FOOTER_LINE_Y, W - MG, FOOTER_LINE_Y)
    c.setFillColor(DARK)
    c.rect(0, 0, W, FOOTER_H, fill=1, stroke=0)
    c.setFillColor(HexColor("#cccccc"))
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(W / 2, 0.27 * inch,
                        "info@jeongai.com  |  (801) 648-9652  |  jeongai.com")
    c.setFillColor(HexColor("#555555"))
    c.setFont("Helvetica", 6.5)
    c.drawRightString(W - MG, 0.27 * inch, str(page_num))


def sec_head(c, x, y, text, color=None):
    clr = color or PRIMARY
    c.setFillColor(clr)
    c.setFont("Helvetica-Bold", 9.5)
    label = text.upper()
    c.drawString(x, y, label)
    c.setStrokeColor(clr)
    c.setLineWidth(0.75)
    tw = c.stringWidth(label, "Helvetica-Bold", 9.5)
    c.line(x, y - 3, x + tw, y - 3)
    return y - 20


def kv_row(c, x, y, label, value, row_w=None, alt=False):
    """Key–value table row with optional alternating background."""
    rw = row_w or (W - 2 * MG)
    if alt:
        c.setFillColor(LIGHT)
        c.rect(x - 6, y - 5, rw + 12, 18, fill=1, stroke=0)
    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 8.5)
    c.drawString(x, y, label)
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(x + 1.6 * inch, y, value)
    return y - 18


def lum(hex_c):
    r = int(hex_c[1:3], 16) / 255
    g = int(hex_c[3:5], 16) / 255
    b = int(hex_c[5:7], 16) / 255
    return 0.299 * r + 0.587 * g + 0.114 * b


def swatch(c, x, y, hex_c, name, var, usage, sw=156, sh=46):
    """Colour swatch with name/hex/var/usage labels."""
    c.setFillColor(HexColor(hex_c))
    c.roundRect(x, y, sw, sh, 4, fill=1, stroke=0)
    tc = WHITE if lum(hex_c) < 0.55 else DARK
    c.setFillColor(tc)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(x + sw / 2, y + sh / 2 + 1, hex_c.upper())
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x, y - 12, name)
    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 7)
    c.drawString(x, y - 22, var)
    c.drawString(x, y - 32, usage[:40])


# ── PAGE 1: COVER ─────────────────────────────────────────────────

def page_cover(c):
    # Full dark background
    c.setFillColor(DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Subtle radial highlight top-right (simulate CSS radial gradient)
    import math
    for i in range(12, 0, -1):
        r_val = i / 12
        alpha = 0.015 * (1 - r_val)
        c.setFillColorRGB(0.04, 0.31, 0.54, alpha)
        radius = 280 * (1 - r_val * 0.4)
        c.circle(W - 60, H - 40, radius, fill=1, stroke=0)

    # Primary blue circle accent behind logo
    c.setFillColor(PRIMARY)
    c.circle(W / 2, H / 2 + 60, 72, fill=1, stroke=0)

    # Inner ring
    c.setFillColor(DARK)
    c.circle(W / 2, H / 2 + 60, 55, fill=1, stroke=0)

    # "정" approximation — stylised J mark
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 44)
    c.drawCentredString(W / 2, H / 2 + 40, "J")
    c.setFillColor(HexColor("#1a6fb8"))
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(W / 2, H / 2 + 22, "Jeong")

    # Brand name large
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 40)
    jw = c.stringWidth("Jeong", "Helvetica-Bold", 40)
    name_x = W / 2 - (jw + c.stringWidth("AI", "Helvetica", 32) + 8) / 2
    c.drawString(name_x, H / 2 - 20, "Jeong")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 32)
    c.drawString(name_x + jw + 8, H / 2 - 13, "AI")

    # Horizontal rule
    c.setStrokeColor(PRIMARY)
    c.setLineWidth(1.5)
    c.line(W / 2 - 80, H / 2 - 38, W / 2 + 80, H / 2 - 38)

    # Document title
    c.setFillColor(HexColor("#aaaaaa"))
    c.setFont("Helvetica", 13)
    c.drawCentredString(W / 2, H / 2 - 60, "Brand & Design Reference")

    # Parent / division
    c.setFillColor(HexColor("#555555"))
    c.setFont("Helvetica", 9)
    c.drawCentredString(W / 2, H / 2 - 80, "A Division of EBYG Media LLC")

    # Bottom info strip
    c.setStrokeColor(PRIMARY)
    c.setLineWidth(0.75)
    c.line(MG, 1.1 * inch, W - MG, 1.1 * inch)
    c.setFillColor(HexColor("#555555"))
    c.setFont("Helvetica", 8)
    c.drawString(MG, 0.85 * inch, "jeongai.com")
    c.drawCentredString(W / 2, 0.85 * inch, "info@jeongai.com  |  (801) 648-9652")
    c.drawRightString(W - MG, 0.85 * inch, "May 2026")

    # Accent bottom bar
    c.setFillColor(PRIMARY_DARK)
    c.rect(0, 0, W, 0.45 * inch, fill=1, stroke=0)
    c.setFillColor(HexColor("#1a6fb8"))
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(W / 2, 0.17 * inch, "Software Is Not One Size Fits All")


# ── PAGE 2: IDENTITY & LOGO ───────────────────────────────────────

def page_identity(c):
    header(c, "Identity & Logo")
    y = BODY_TOP

    y = sec_head(c, MG, y, "Brand Identity")

    rows = [
        ("Brand Name", "Jeong AI"),
        ("Parent Company", "EBYG Media LLC"),
        ("Tagline", "Software Is Not One Size Fits All"),
        ("Meta Title", "Jeong AI — Custom Software & AI Tools Built for Your Business"),
        ("Domain", "jeongai.com"),
        ("Phone", "(801) 648-9652"),
        ("Email", "info@jeongai.com"),
        ("Address", "Fully remote — no physical address"),
    ]
    for i, (label, value) in enumerate(rows):
        y = kv_row(c, MG, y, label, value, alt=(i % 2 == 0))

    y -= 20
    y = sec_head(c, MG, y, "Logo Construction")

    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 8.5)
    c.drawString(MG, y, "Text-only — no image file exists. Two adjacent spans on the same baseline:")
    y -= 22

    # Logo demo box
    box_h = 0.95 * inch
    c.setFillColor(LIGHT)
    c.roundRect(MG, y - box_h, W - 2 * MG, box_h, 6, fill=1, stroke=0)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.roundRect(MG, y - box_h, W - 2 * MG, box_h, 6, fill=0, stroke=1)

    logo_y = y - box_h / 2 - 10
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 28)
    jw = c.stringWidth("Jeong", "Helvetica-Bold", 28)
    c.drawString(MG + 0.5 * inch, logo_y, "Jeong")
    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 22)
    c.drawString(MG + 0.5 * inch + jw + 5, logo_y + 4, "AI")

    # Annotations
    c.setFillColor(ACCENT)
    c.setFont("Helvetica", 7)
    ann_y = logo_y - 16
    c.drawString(MG + 0.5 * inch, ann_y, '"Jeong"  Helvetica-Bold  28pt  #0a4f8a  --primary')
    c.drawString(MG + 0.5 * inch + jw + 5, ann_y, '"AI"  Helvetica  22pt  #6b6b7b  --text-light')

    y = y - box_h - 20
    y = sec_head(c, MG, y, "Brand Symbol")

    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 8.5)
    lines = [
        "The Korean character  정 (jeong)  represents warmth, care, and genuine human relationship.",
        "It is used as a decorative brand symbol in select UI contexts — not as the primary logo mark.",
        "Brand meaning: showing up consistently, caring genuinely, being quietly reliable.",
    ]
    for line in lines:
        c.drawString(MG, y, line)
        y -= 14

    y -= 14
    y = sec_head(c, MG, y, "Two-Brand Structure")

    col_w = (W - 2 * MG - 16) / 2

    # Brand card 1
    bx1 = MG
    by = y - 1.1 * inch
    c.setFillColor(LIGHT)
    c.roundRect(bx1, by, col_w, 1.05 * inch, 6, fill=1, stroke=0)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.roundRect(bx1, by, col_w, 1.05 * inch, 6, fill=0, stroke=1)
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(bx1 + 10, by + 70, "JEONG AI — AUTOMATION")
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 8)
    c.drawString(bx1 + 10, by + 55, "Custom software, AI agents,")
    c.drawString(bx1 + 10, by + 43, "and automated workflows.")
    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica-Oblique", 7.5)
    c.drawString(bx1 + 10, by + 27, "Audience: Business owners who need")
    c.drawString(bx1 + 10, by + 16, "custom solutions.")

    # Brand card 2
    bx2 = MG + col_w + 16
    c.setFillColor(PRIMARY)
    c.roundRect(bx2, by, col_w, 1.05 * inch, 6, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(bx2 + 10, by + 70, "JEONG AI — EDUCATION")
    c.setFont("Helvetica", 8)
    c.drawString(bx2 + 10, by + 55, "AI education and learning")
    c.drawString(bx2 + 10, by + 43, "programs.")
    c.setFillColor(HexColor("#aaccee"))
    c.setFont("Helvetica-Oblique", 7.5)
    c.drawString(bx2 + 10, by + 27, "Audience: Individuals learning AI.")
    c.drawString(bx2 + 10, by + 16, "Graduates into the service side.")

    # Arrow between cards
    arrow_x = MG + col_w + 8
    arrow_y = by + 0.52 * inch
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(arrow_x, arrow_y, arrow_x + 16, arrow_y)
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(arrow_x + 8, arrow_y - 10, "→")

    footer(c, 2)


# ── PAGE 3: COLOR PALETTE ─────────────────────────────────────────

def page_colors(c):
    header(c, "Color Palette")
    y = BODY_TOP

    # ── Primary Colors ──
    y = sec_head(c, MG, y, "Primary Colors")

    sw = 156
    gap = (W - 2 * MG - 3 * sw) / 2
    colors_primary = [
        ("#0a4f8a", "Primary Blue",  "--primary",       "Buttons, links, icons, borders"),
        ("#083d6b", "Primary Dark",  "--primary-dark",  "Gradient ends, hover states"),
        ("#1a6fb8", "Primary Light", "--primary-light", "Text on dark backgrounds"),
    ]
    for i, (hx, nm, var, use) in enumerate(colors_primary):
        x = MG + i * (sw + gap)
        swatch(c, x, y - 46, hx, nm, var, use, sw=sw)
    y -= 46 + 46

    # ── Accent Colors ──
    y = sec_head(c, MG, y, "Accent Colors")

    sw2 = 170
    gap2 = (W - 2 * MG - 2 * sw2)
    colors_accent = [
        ("#c7553b", "Accent Red-Orange", "--accent",       "CTA buttons, pricing, badges"),
        ("#a8432d", "Accent Hover",      "--accent-hover", "Hover state on accent elements"),
    ]
    for i, (hx, nm, var, use) in enumerate(colors_accent):
        x = MG + i * (sw2 + gap2)
        swatch(c, x, y - 46, hx, nm, var, use, sw=sw2)
    y -= 46 + 46

    # ── Neutral / Background Colors ──
    y = sec_head(c, MG, y, "Neutral & Background Colors")

    sw3 = 130
    gap3 = (W - 2 * MG - 4 * sw3) / 3
    colors_neutral = [
        ("#1a1a2e", "Dark Navy",     "--dark",         "Footer, dark sections"),
        ("#3a3a4a", "Body Text",     "--text",         "All body copy"),
        ("#6b6b7b", "Light Text",    "--text-light",   "Captions, descriptions"),
        ("#f7f8fa", "Light BG",      "--light",        "Alt section backgrounds"),
    ]
    for i, (hx, nm, var, use) in enumerate(colors_neutral):
        x = MG + i * (sw3 + gap3)
        swatch(c, x, y - 46, hx, nm, var, use, sw=sw3)
    y -= 46 + 14

    sw4 = 130
    colors_neutral2 = [
        ("#f2ede3", "Warm BG",       "(inline)",       "Conviction/quote sections"),
        ("#ffffff", "White",         "--white",        "Cards, page bg, text on dark"),
        ("#e2e4e8", "Border",        "--border",       "Card borders, dividers"),
        ("#aaaaaa", "Muted Gray",    "(muted)",        "Subdued labels, secondary"),
    ]
    for i, (hx, nm, var, use) in enumerate(colors_neutral2):
        x = MG + i * (sw4 + gap3)
        swatch(c, x, y - 46, hx, nm, var, use, sw=sw4)

    # Draw border on white swatch so it's visible
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    wx = MG + 1 * (sw4 + gap3)
    c.roundRect(wx, y - 46, sw4, 46, 4, fill=0, stroke=1)

    y -= 46 + 46

    # ── Extended / Purple Palette ──
    y = sec_head(c, MG, y, "Extended Palette (Available — Rarely Used on Main Site)")

    sw5 = 116
    gap5 = (W - 2 * MG - 4 * sw5) / 3
    colors_purple = [
        ("#7C3AED", "Purple",       "--purple",        "Available"),
        ("#8B5CF6", "Purple Mid",   "--purple-mid",    "Available"),
        ("#EDE9FE", "Purple Light", "--purple-light",  "Available"),
        ("#F5F3FF", "Purple Pale",  "--purple-pale",   "Available"),
    ]
    for i, (hx, nm, var, use) in enumerate(colors_purple):
        x = MG + i * (sw5 + gap5)
        swatch(c, x, y - 46, hx, nm, var, use, sw=sw5)

    # borders on light purple swatches
    for i in [2, 3]:
        px = MG + i * (sw5 + gap5)
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.5)
        c.roundRect(px, y - 46, sw5, 46, 4, fill=0, stroke=1)

    footer(c, 3)


# ── PAGE 4: TYPOGRAPHY + TOKENS ───────────────────────────────────

def page_type_tokens(c):
    header(c, "Typography & Design Tokens")
    y = BODY_TOP

    # ── Typography ──
    col_l = MG
    col_r = W / 2 + 8

    y = sec_head(c, col_l, y, "Typography")

    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 8)
    c.drawString(col_l, y, "Headings: Montserrat (400/500/600/700)  ·  Body: Source Sans 3 / Source Sans Pro (300/400/500/600)")
    y -= 14

    type_scale = [
        ("h1", "Helvetica-Bold", 26, "#1a1a2e", "3.2rem → responsive"),
        ("h2", "Helvetica-Bold", 20, "#1a1a2e", "2.4rem → responsive"),
        ("h3", "Helvetica-Bold", 14, "#1a1a2e", "1.4rem"),
        ("h4", "Helvetica-Bold", 11, "#1a1a2e", "1.1rem"),
        ("Body", "Helvetica",    9,  "#3a3a4a", "17px · 1.65 line-height"),
        ("Lead", "Helvetica",    9,  "#6b6b7b", "1.15rem · 1.7 line-height"),
        ("Tag",  "Helvetica-Bold", 7, "#0a4f8a", "0.8rem · uppercase · 2px spacing"),
    ]

    for tag, font, size, hex_c, note in type_scale:
        c.setFillColor(HexColor(hex_c))
        c.setFont(font, size)
        sample = f"{tag}" if tag in ("Body", "Lead", "Tag") else f"Aa — {tag}"
        c.drawString(col_l, y, sample)
        c.setFillColor(TEXT_LIGHT)
        c.setFont("Helvetica", 7)
        c.drawRightString(col_r - 20, y, note)
        y -= size + 5
        if tag not in ("Tag",):
            y -= 2

    y -= 12

    # ── Gradients ──
    y = sec_head(c, col_l, y, "Gradients")

    gw = (col_r - col_l - 12) / 2 - 8
    gh = 30

    # Primary gradient swatch
    c.setFillColor(HexColor("#0a4f8a"))
    c.roundRect(col_l, y - gh, gw, gh, 4, fill=1, stroke=0)
    # Simulate gradient overlay
    c.setFillColor(HexColor("#083d6b"))
    c.roundRect(col_l + gw * 0.5, y - gh, gw * 0.5, gh, 4, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(col_l + gw / 2, y - gh / 2 - 3, "Primary Gradient")

    # Hero bg gradient swatch
    c.setFillColor(HexColor("#f0f4f8"))
    c.roundRect(col_l + gw + 12, y - gh, gw, gh, 4, fill=1, stroke=0)
    c.setFillColor(HexColor("#dce4ef"))
    c.roundRect(col_l + gw + 12 + gw * 0.5, y - gh, gw * 0.5, gh, 4, fill=1, stroke=0)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.roundRect(col_l + gw + 12, y - gh, gw, gh, 4, fill=0, stroke=1)
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(col_l + gw + 12 + gw / 2, y - gh / 2 - 3, "Hero Background")

    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 6.5)
    c.drawString(col_l, y - gh - 10, "135deg · #0a4f8a → #083d6b")
    c.drawString(col_l + gw + 12, y - gh - 10, "135deg · #f0f4f8 → #e8edf4 → #dce4ef")

    y -= gh + 24

    # ─── RIGHT COLUMN ───────────────────────────────────────────────

    col_r_start = W / 2 + 8
    y_r = BODY_TOP

    y_r = sec_head(c, col_r_start, y_r, "Spacing & Layout")

    layout_rows = [
        ("Max width",         "1200px"),
        ("Header height",     "80px"),
        ("Section padding",   "6rem 0 (4rem tablet, 3rem mobile)"),
        ("Container padding", "0 2rem (0 1.25rem mobile)"),
        ("Border radius sm",  "6px"),
        ("Border radius lg",  "12px"),
        ("Transition",        "0.25s ease"),
    ]
    for i, (label, value) in enumerate(layout_rows):
        y_r = kv_row(c, col_r_start, y_r, label, value,
                     row_w=W - col_r_start - MG, alt=(i % 2 == 0))

    y_r -= 16
    y_r = sec_head(c, col_r_start, y_r, "Shadows")

    shadow_rows = [
        ("--shadow-sm", "0 1px 3px rgba(0,0,0,0.06)"),
        ("--shadow-md", "0 4px 16px rgba(0,0,0,0.08)"),
        ("--shadow-lg", "0 8px 32px rgba(0,0,0,0.12)"),
        ("--shadow-xl", "0 16px 48px rgba(0,0,0,0.14)"),
    ]
    for i, (label, value) in enumerate(shadow_rows):
        y_r = kv_row(c, col_r_start, y_r, label, value,
                     row_w=W - col_r_start - MG, alt=(i % 2 == 0))

    y_r -= 16
    y_r = sec_head(c, col_r_start, y_r, "Buttons")

    btn_data = [
        ("btn-primary",  PRIMARY,  WHITE,   PRIMARY,  "Primary", "btn-primary hover → accent"),
        ("btn-outline",  WHITE,    PRIMARY, PRIMARY,  "Outline", "Hover → filled primary"),
        ("btn (dark bg)", DARK,    HexColor("#cccccc"), HexColor("#555555"), "On dark", "Hover → filled primary"),
    ]
    btn_y = y_r
    for font_c, bg_c, txt_c, border_c, label, note in btn_data:
        bw = 120
        bh = 22
        c.setFillColor(bg_c)
        c.roundRect(col_r_start, btn_y - bh, bw, bh, 4, fill=1, stroke=0)
        c.setStrokeColor(border_c)
        c.setLineWidth(1.2)
        c.roundRect(col_r_start, btn_y - bh, bw, bh, 4, fill=0, stroke=1)
        c.setFillColor(txt_c)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(col_r_start + bw / 2, btn_y - bh / 2 - 3, label)
        c.setFillColor(TEXT_LIGHT)
        c.setFont("Helvetica", 7)
        c.drawString(col_r_start + bw + 8, btn_y - bh / 2 - 3, note)
        btn_y -= bh + 10

    # divider between columns
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(W / 2, BODY_BTM + 10, W / 2, BODY_TOP + 4)

    footer(c, 4)


# ── PAGE 5: VOICE & CONTACT ───────────────────────────────────────

def page_voice(c):
    header(c, "Brand Voice & Contact")
    y = BODY_TOP

    col_l = MG
    col_r = W / 2 + 8
    col_w = W / 2 - MG - 8

    # ── Left: Brand Voice ──────────────────────────────────────────
    y = sec_head(c, col_l, y, "Brand Voice & Tone")

    voice_attrs = [
        ("Direct + Confident",    "No fluff, no buzzword soup. Say what you mean."),
        ("Business-First",        "Lead with outcomes and client benefit, not features."),
        ("Warm but Professional", "Genuine care — not cold tech, not casual chat."),
        ("Specific",              "\"built for your business, not the other 10,000\""),
        ("Anti-hype",             "Avoid vague AI promises and generic SaaS language."),
    ]

    for i, (attr, desc) in enumerate(voice_attrs):
        if i % 2 == 0:
            c.setFillColor(LIGHT)
            c.rect(col_l - 6, y - 5, col_w + 12, 30, fill=1, stroke=0)
        c.setFillColor(PRIMARY)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(col_l, y, attr)
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 8)
        c.drawString(col_l, y - 12, desc)
        y -= 32

    y -= 10
    y = sec_head(c, col_l, y, "Key Phrases (Reuse These)")

    phrases = [
        "\"Software is not one size fits all\"",
        "\"Built around how your business actually works\"",
        "\"Your systems, not ours\"",
        "\"정 (jeong)\" — warmth, care, genuine relationship",
    ]
    for phrase in phrases:
        c.setFillColor(PRIMARY)
        c.rect(col_l - 6, y - 4, 3, 14, fill=1, stroke=0)
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 8.5)
        c.drawString(col_l + 6, y, phrase)
        y -= 18

    y -= 10
    y = sec_head(c, col_l, y, "Avoid")

    avoid = [
        "Generic SaaS language",
        "Vague AI/tech buzzwords",
        "Hype or overstatement",
        "Jargon without context",
    ]
    for item in avoid:
        c.setFillColor(ACCENT)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(col_l, y, "×")
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 8.5)
        c.drawString(col_l + 14, y, item)
        y -= 16

    # ── Right: Canonical Contact + Meta ───────────────────────────
    y_r = BODY_TOP
    y_r = sec_head(c, col_r, y_r, "Canonical Contact Info")

    contact_rows = [
        ("Business",  "Jeong AI"),
        ("Parent",    "EBYG Media LLC"),
        ("Phone",     "(801) 648-9652"),
        ("Email",     "info@jeongai.com"),
        ("Website",   "jeongai.com"),
        ("Address",   "Fully remote — not displayed"),
        ("Social",    "None currently"),
    ]
    for i, (label, value) in enumerate(contact_rows):
        y_r = kv_row(c, col_r, y_r, label, value,
                     row_w=W - col_r - MG, alt=(i % 2 == 0))

    y_r -= 20
    y_r = sec_head(c, col_r, y_r, "Meta / SEO Reference")

    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 7.5)
    c.drawString(col_r, y_r, "OG Title:")
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 7.5)
    og_title = "Jeong AI — Custom Software & AI Tools"
    c.drawString(col_r + 0.65 * inch, y_r, og_title)
    y_r -= 13

    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 7.5)
    c.drawString(col_r, y_r, "OG Site:")
    c.setFillColor(TEXT)
    c.drawString(col_r + 0.65 * inch, y_r, "Jeong AI")
    y_r -= 13

    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 7.5)
    c.drawString(col_r, y_r, "Locale:")
    c.setFillColor(TEXT)
    c.drawString(col_r + 0.65 * inch, y_r, "en_US")
    y_r -= 22

    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 7.5)
    desc_text = ("Software is not one size fits all. Custom software,")
    c.drawString(col_r, y_r, "Description:")
    y_r -= 12
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 7.5)
    for line in [
        "Software is not one size fits all.",
        "Custom software, AI agents, and automated",
        "workflows built precisely around how your",
        "business works.",
    ]:
        c.drawString(col_r + 10, y_r, line)
        y_r -= 12

    y_r -= 14
    y_r = sec_head(c, col_r, y_r, "CSS Custom Properties (Quick Ref)")

    css_rows = [
        ("--primary",      "#0a4f8a"),
        ("--primary-dark", "#083d6b"),
        ("--accent",       "#c7553b"),
        ("--dark",         "#1a1a2e"),
        ("--text",         "#3a3a4a"),
        ("--text-light",   "#6b6b7b"),
        ("--light",        "#f7f8fa"),
        ("--border",       "#e2e4e8"),
        ("--font-heading", "Montserrat, sans-serif"),
        ("--font-body",    "Source Sans 3, sans-serif"),
        ("--max-width",    "1200px"),
        ("--header-h",     "80px"),
    ]
    for i, (prop, val) in enumerate(css_rows):
        if i % 2 == 0:
            c.setFillColor(LIGHT)
            c.rect(col_r - 6, y_r - 4, W - col_r - MG + 12, 14, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.setFont("Helvetica", 7.5)
        c.drawString(col_r, y_r, prop)
        c.setFillColor(TEXT)
        c.drawString(col_r + 1.2 * inch, y_r, val)
        y_r -= 13

    # Divider
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(W / 2, BODY_BTM + 10, W / 2, BODY_TOP + 4)

    footer(c, 5)


# ── MAIN ──────────────────────────────────────────────────────────

def main():
    c = pdf_canvas.Canvas(OUTPUT, pagesize=letter)
    c.setTitle("JeongAI Brand & Design Reference")
    c.setAuthor("Jeong AI")
    c.setSubject("Brand guidelines, color palette, typography, and design tokens")

    page_cover(c);   c.showPage()
    page_identity(c); c.showPage()
    page_colors(c);   c.showPage()
    page_type_tokens(c); c.showPage()
    page_voice(c);    c.showPage()

    c.save()
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    main()
