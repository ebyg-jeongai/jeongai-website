"""
Generate: AI Prompt Building Guide for HR Managers
Brand: Jeong AI (matches www.jeongai.com style)
Output: vault/docs/templates/HR-AI-Prompt-Building-Guide.pdf
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

W, H = letter  # 612 x 792

# ── Brand colors ──
DARK_NAVY   = HexColor("#2a2a45")
ACCENT_BLUE = HexColor("#3a86ff")
ACCENT_GOLD = HexColor("#d4a843")
MEDIUM_GRAY = HexColor("#555555")
LIGHT_GRAY  = HexColor("#e0e0e0")
WHITE       = HexColor("#ffffff")
MUTED_GRAY  = HexColor("#aaaaaa")
LIGHT_BG    = HexColor("#f4f5f7")

# ── Layout constants ──
MARGIN = 0.75 * inch
HEADER_H = 1.4 * inch
FOOTER_BAR_H = 0.65 * inch
GOLD_LINE_Y = H - HEADER_H - 2
FOOTER_GOLD_Y = FOOTER_BAR_H + 0.25 * inch
BODY_TOP = GOLD_LINE_Y - 0.4 * inch
BODY_W = W - 2 * MARGIN

# ── Spacing constants ──
LINE_HEIGHT = 16          # body text leading
SECTION_GAP = 20          # space before a new section header
CRAFT_LINE_H = 17         # CRAFT framework row height
BULLET_LINE_H = 19        # bullet point row height
BOX_LINE_H = 14           # line height inside prompt boxes
BOX_PAD_TOP = 18          # padding above label inside box
BOX_PAD_BOTTOM = 10       # padding below last line inside box
BOX_LABEL_GAP = 16        # gap between label and first text line
BOX_GAP_AFTER = 14        # space after a prompt box


def draw_header(c):
    """Dark navy header bar with branding and contact info."""
    c.setFillColor(DARK_NAVY)
    c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)

    # Gold accent line
    c.setStrokeColor(ACCENT_GOLD)
    c.setLineWidth(2.5)
    c.line(0, GOLD_LINE_Y, W, GOLD_LINE_Y)

    # Company name
    x_left = MARGIN
    y_name = H - 0.55 * inch
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(WHITE)
    jai_w = c.stringWidth("Jeong AI", "Helvetica-Bold", 28)
    c.drawString(x_left, y_name, "Jeong AI")

    # Tagline
    c.setFont("Helvetica-Oblique", 9.5)
    c.setFillColor(ACCENT_GOLD)
    c.drawString(x_left, y_name - 16, "AI Systems & Custom Software Solutions")

    # Division subtitle
    c.setFont("Helvetica", 7.5)
    c.setFillColor(MUTED_GRAY)
    c.drawString(x_left, y_name - 28, "A Division of EBYG Media LLC")

    # Contact info (right-aligned)
    x_right = W - MARGIN
    c.setFont("Helvetica", 9)
    c.setFillColor(WHITE)
    c.drawRightString(x_right, H - 0.45 * inch, "(801) 648-9652")
    c.drawRightString(x_right, H - 0.62 * inch, "info@jeongai.com")
    c.drawRightString(x_right, H - 0.79 * inch, "www.jeongai.com")


def draw_footer(c):
    """Dark navy footer bar with contact info and philosophy tagline."""
    c.setFillColor(DARK_NAVY)
    c.rect(0, 0, W, FOOTER_BAR_H, fill=1, stroke=0)

    # Gold line above footer
    c.setStrokeColor(ACCENT_GOLD)
    c.setLineWidth(2)
    c.line(MARGIN, FOOTER_GOLD_Y, W - MARGIN, FOOTER_GOLD_Y)

    # Contact line
    c.setFont("Helvetica", 7.5)
    c.setFillColor(LIGHT_GRAY)
    c.drawCentredString(W / 2, 0.38 * inch,
                        "(801) 648-9652  |  info@jeongai.com  |  www.jeongai.com")

    # Philosophy tagline
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColor(ACCENT_GOLD)
    c.drawCentredString(W / 2, 0.22 * inch,
                        "Consistent presence. Genuine care. Quiet reliability.")


def draw_section_header(c, y, text):
    """Accent blue section header with gold underline."""
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(DARK_NAVY)
    c.drawString(MARGIN, y, text)
    c.setStrokeColor(ACCENT_GOLD)
    c.setLineWidth(1)
    c.line(MARGIN, y - 5, MARGIN + c.stringWidth(text, "Helvetica-Bold", 13) + 8, y - 5)
    return y - 26


def draw_body_text(c, y, text, font="Helvetica", size=10, color=MEDIUM_GRAY, indent=0):
    """Draw a line of body text, return new y position."""
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawString(MARGIN + indent, y, text)
    return y - LINE_HEIGHT


def draw_bullet(c, y, text, indent=14, line_h=None):
    """Draw a bullet point."""
    c.setFont("Helvetica", 10)
    c.setFillColor(MEDIUM_GRAY)
    c.drawString(MARGIN + indent, y, "\u2022")
    c.drawString(MARGIN + indent + 14, y, text)
    return y - (line_h if line_h is not None else BULLET_LINE_H)


def wrap_text(c, text, font, size, max_w):
    """Word-wrap text into lines that fit within max_w."""
    lines = []
    words = text.split()
    line = ""
    for w in words:
        test = line + (" " if line else "") + w
        if c.stringWidth(test, font, size) < max_w:
            line = test
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def draw_prompt_box(c, y, label, prompt_text, gap_after=None):
    """Draw a branded example prompt box with comfortable spacing."""
    box_w = BODY_W
    text_w = box_w - 28  # 14px padding each side
    lines = wrap_text(c, prompt_text, "Helvetica", 9, text_w)

    box_h = BOX_PAD_TOP + BOX_LABEL_GAP + (len(lines) * BOX_LINE_H) + BOX_PAD_BOTTOM

    # Box background
    c.setFillColor(LIGHT_BG)
    c.setStrokeColor(ACCENT_BLUE)
    c.setLineWidth(0.75)
    c.roundRect(MARGIN, y - box_h, box_w, box_h, 4, fill=1, stroke=1)

    # Label
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ACCENT_BLUE)
    c.drawString(MARGIN + 14, y - BOX_PAD_TOP, label)

    # Prompt text
    c.setFont("Helvetica", 9)
    c.setFillColor(MEDIUM_GRAY)
    ty = y - BOX_PAD_TOP - BOX_LABEL_GAP
    for line in lines:
        c.drawString(MARGIN + 14, ty, line)
        ty -= BOX_LINE_H

    return y - box_h - (gap_after if gap_after is not None else BOX_GAP_AFTER)


def build_page1(c):
    """Page 1: Title, intro, The CRAFT Framework, first examples."""
    draw_header(c)
    draw_footer(c)

    y = BODY_TOP

    # Document title
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(DARK_NAVY)
    c.drawString(MARGIN, y, "AI Prompt Building for HR Managers")
    y -= 22

    c.setFont("Helvetica", 11)
    c.setFillColor(ACCENT_BLUE)
    c.drawString(MARGIN, y, "A Practical Guide to Getting Better Results from AI Tools")
    y -= 32

    # Intro paragraph
    intro_lines = [
        "AI tools like ChatGPT, Claude, and Copilot can save HR teams hours each week \u2014 but only",
        "if you know how to communicate with them effectively. The difference between a vague prompt",
        "and a structured one is the difference between generic filler and a usable first draft.",
    ]
    for line in intro_lines:
        y = draw_body_text(c, y, line)
    y -= 8

    y = draw_body_text(c, y, "This guide gives you a repeatable framework and real HR examples you can use immediately.")
    y -= SECTION_GAP

    # ── Section 1: The CRAFT Framework ──
    y = draw_section_header(c, y, "The CRAFT Framework")

    craft_items = [
        ("C \u2014 Context:", "Who are you? What\u2019s the situation?"),
        ("R \u2014 Role:", "Who should the AI act as?"),
        ("A \u2014 Action:", "What exactly do you want it to do?"),
        ("F \u2014 Format:", "How should the output be structured?"),
        ("T \u2014 Tone:", "What voice or style should it use?"),
    ]
    for bold_part, rest in craft_items:
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(DARK_NAVY)
        c.drawString(MARGIN + 14, y, bold_part)
        bw = c.stringWidth(bold_part, "Helvetica-Bold", 10)
        c.setFont("Helvetica", 10)
        c.setFillColor(MEDIUM_GRAY)
        c.drawString(MARGIN + 14 + bw + 5, y, rest)
        y -= CRAFT_LINE_H

    y -= SECTION_GAP

    # ── Section 2: Before & After ──
    y = draw_section_header(c, y, "Before & After: See the Difference")

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(HexColor("#cc3333"))
    c.drawString(MARGIN, y, "Weak Prompt:")
    y -= 10
    y = draw_prompt_box(c, y, "EXAMPLE \u2014 WEAK",
                        "Write me a job description for a marketing person.")

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(HexColor("#228833"))
    c.drawString(MARGIN, y, "Strong Prompt (using CRAFT):")
    y -= 10
    y = draw_prompt_box(c, y, "EXAMPLE \u2014 STRONG",
                        "Context: I\u2019m an HR Manager at a 200-person SaaS company hiring for our first dedicated "
                        "marketing role. Role: Act as a senior HR copywriter with tech industry experience. "
                        "Action: Write a job description for a Marketing Manager. Include responsibilities, "
                        "qualifications (must-have vs. nice-to-have), and a compelling company culture section. "
                        "Format: Use headers, bullet points, and keep it under 600 words. "
                        "Tone: Professional but approachable \u2014 we\u2019re a startup, not a bank.")

    # Quick tip
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(ACCENT_GOLD)
    tip_label = "Pro Tip:  "
    c.drawString(MARGIN, y, tip_label)
    c.setFont("Helvetica-Oblique", 9.5)
    c.setFillColor(MEDIUM_GRAY)
    c.drawString(MARGIN + c.stringWidth(tip_label, "Helvetica-Bold", 9.5), y,
                 "You can always follow up with \u201cMake it shorter,\u201d \u201cAdd a DEI statement,\u201d or \u201cMake the tone more formal.\u201d")


def build_page2(c):
    """Page 2: HR-specific prompt templates and next steps."""
    c.showPage()
    draw_header(c)
    draw_footer(c)

    y = BODY_TOP

    # ── Section: Ready-to-Use HR Prompts ──
    y = draw_section_header(c, y, "Ready-to-Use HR Prompt Templates")

    templates = [
        ("1. Policy Drafting",
         "Context: Our 150-employee company has no formal remote work policy. Role: Act as an HR policy "
         "specialist. Action: Draft a remote/hybrid work policy covering eligibility, expectations, "
         "equipment, and communication norms. Format: Numbered sections with headers. Tone: Clear and "
         "firm but employee-friendly."),

        ("2. Interview Questions",
         "Context: I\u2019m interviewing candidates for a Senior Accountant role. Role: Act as a behavioral "
         "interview expert. Action: Generate 8 interview questions \u2014 4 behavioral, 2 situational, "
         "2 technical. Format: Numbered list with a brief note on what each question evaluates. "
         "Tone: Conversational but structured."),

        ("3. Employee Communication",
         "Context: We\u2019re switching health insurance providers effective next quarter. Role: Act as an "
         "internal communications specialist. Action: Write an employee announcement email explaining "
         "the change, what stays the same, what\u2019s new, and next steps. Format: Short paragraphs with "
         "a bullet-point summary of key changes. Tone: Reassuring and transparent."),

        ("4. Performance Review Assistance",
         "Context: I need to write a constructive performance review for an employee who exceeds "
         "technical goals but struggles with collaboration. Role: Act as a seasoned HR business partner. "
         "Action: Write a balanced performance review summary with strengths, growth areas, and 2\u20133 "
         "specific development goals. Format: Three sections \u2014 Strengths, Areas for Growth, Goals. "
         "Tone: Supportive, specific, and development-focused."),
    ]

    for title, prompt in templates:
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(DARK_NAVY)
        c.drawString(MARGIN, y, title)
        y -= 10
        y = draw_prompt_box(c, y, "TEMPLATE", prompt, gap_after=16)

    y -= 2

    # ── Section: Key Principles ──
    y = draw_section_header(c, y, "Five Rules for Better AI Prompts")

    rules = [
        "Be specific \u2014 vague input equals vague output. Include numbers, names, and constraints.",
        "Assign a role \u2014 telling AI \u201cwho to be\u201d dramatically improves quality.",
        "Iterate \u2014 your first prompt is a starting point. Refine with follow-ups.",
        "Protect sensitive data \u2014 never paste employee SSNs, salaries, or PII into AI tools.",
        "Verify everything \u2014 AI can be confidently wrong. Always review before using.",
    ]
    for rule in rules:
        y = draw_bullet(c, y, rule, line_h=15)

    y -= 8

    # ── CTA box ──
    cta_h = 48
    c.setFillColor(LIGHT_BG)
    c.setStrokeColor(ACCENT_BLUE)
    c.setLineWidth(1)
    c.roundRect(MARGIN, y - cta_h, BODY_W, cta_h, 4, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(DARK_NAVY)
    c.drawCentredString(W / 2, y - 18, "Want help building AI workflows for your HR team?")
    c.setFont("Helvetica", 10)
    c.setFillColor(ACCENT_BLUE)
    c.drawCentredString(W / 2, y - 34,
                        "Book a free automation audit at www.jeongai.com  |  info@jeongai.com")


def main():
    output = "vault/docs/templates/HR-AI-Prompt-Building-Guide.pdf"
    c = canvas.Canvas(output, pagesize=letter)
    c.setTitle("AI Prompt Building for HR Managers — Jeong AI")
    c.setAuthor("Jeong AI")
    c.setSubject("A practical guide to building effective AI prompts for HR professionals")

    build_page1(c)
    build_page2(c)

    c.save()
    print(f"Generated: {output}")


if __name__ == "__main__":
    main()
