# Homepage Custom Software Reframe — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reframe index.html from "AI Systems" to custom software/AI agents/tools with "software is not one size fits all" as the central argument — adding 2 new sections, replacing 2 existing sections, and updating hero copy.

**Architecture:** Pure HTML/CSS edits to `index.html` and `css/styles.css`. No build tools, no frameworks. Local preview at http://localhost:8080. Each task targets one section; verify in browser after each before committing.

**Tech Stack:** Static HTML, CSS custom properties (already established in styles.css), Google Fonts (Montserrat + Source Sans 3 already loaded)

---

## File Map

| File | Changes |
|------|---------|
| `index.html` | Update `<head>` meta/title; update hero h1 + subhead + CTA; add OSFA section; replace ecosystem section with What We Build; add Custom Software deep-dive; replace advantage section with Conviction |
| `css/styles.css` | Add styles for `.osfa`, `.wwb-*`, `.custom-software`/`.cs-*`, `.conviction`; update responsive rules |

---

## Task 1: Update Meta Tags and Hero Copy

**Files:**
- Modify: `index.html` lines 6–12 (meta/title)
- Modify: `index.html` lines 49–53 (hero h1, subhead, CTAs)

- [ ] **Step 1: Update page title and meta description**

Replace lines 6–12 in `index.html`:

```html
  <meta name="description" content="Software is not one size fits all. Jeong AI builds custom software, AI agents, and automated workflows precisely around how your business works — not the other way around.">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Jeong AI — Custom Software & AI Tools Built for Your Business">
  <meta property="og:description" content="Software is not one size fits all. Custom software, AI agents, and automated workflows built precisely around how your business works.">
  <meta property="og:site_name" content="Jeong AI">
  <meta property="og:locale" content="en_US">
  <title>Jeong AI — Custom Software &amp; AI Tools Built for Your Business</title>
```

- [ ] **Step 2: Update hero headline**

Replace line 49:
```html
      <h1>Software Is Not<br><span class="highlight">One Size Fits All.</span></h1>
```

- [ ] **Step 3: Update hero subhead**

Replace line 50:
```html
      <p class="hero-sub">The tools running your business should be built for your business — not the other ten thousand companies on the same SaaS. We build AI agents, custom software, and automated workflows that fit exactly.</p>
```

- [ ] **Step 4: Update hero CTAs**

Replace lines 52–53:
```html
        <a href="#contact" class="btn btn-primary">Book a Free Automation Audit</a>
        <a href="#what-we-build" class="btn btn-outline">See What We Build</a>
```

- [ ] **Step 5: Verify in browser**

Open http://localhost:8080 — confirm:
- Hero headline reads "Software Is Not / One Size Fits All."
- Subhead reads "The tools running your business..."
- Second CTA says "See What We Build"
- Page tab title updated

- [ ] **Step 6: Commit**

```bash
cd /c/Users/Derrick/ebygautomation && git add index.html && git commit -m "Update hero copy — software is not one size fits all"
```

---

## Task 2: Add OSFA Argument Section + CSS

**Files:**
- Modify: `index.html` — insert new section after line 84 (closing `</section>` of trust-bar)
- Modify: `css/styles.css` — add `.osfa` styles after `/* ---------- TRUST BAR ---------- */` block

- [ ] **Step 1: Insert OSFA section into index.html**

After the closing `</section>` tag of the trust-bar (after line 84), insert:

```html
  <!-- ========== NOT ONE SIZE FITS ALL ========== -->
  <section class="osfa">
    <div class="container">
      <div class="osfa-inner">
        <p class="section-tag osfa-tag">The Problem With Off-The-Shelf</p>
        <h2 class="osfa-heading">Most software is built for <em>everyone</em>.<br>That means it's built for <em>no one</em>.</h2>
        <div class="osfa-grid">
          <div class="osfa-card">
            <h4>Generic SaaS</h4>
            <p>You adapt your process to fit the tool. Workarounds become permanent. Friction compounds.</p>
          </div>
          <div class="osfa-card">
            <h4>Stitched-Together Automations</h4>
            <p>Zapier chains that break. Integrations that drift. A patchwork that no one fully understands.</p>
          </div>
          <div class="osfa-card osfa-card-jeong">
            <h4>The Jeong Way</h4>
            <p>We build the tool around your workflow. Custom software, AI agents, and automation that fit exactly &mdash; because they were built for exactly you.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Add OSFA CSS to styles.css**

After the closing brace of the `/* ---------- TRUST BAR ---------- */` block (after `.trust-label { ... }`), insert:

```css
/* ---------- OSFA (Not One Size Fits All) ---------- */
.osfa {
  padding: 6rem 0;
  background: var(--dark);
}
.osfa-inner { text-align: center; }
.osfa-tag { color: rgba(255,255,255,0.45) !important; }
.osfa-heading {
  color: var(--white);
  font-size: 2.4rem;
  margin-bottom: 3rem;
  line-height: 1.25;
}
.osfa-heading em {
  color: var(--primary-light);
  font-style: italic;
}
.osfa-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  text-align: left;
}
.osfa-card {
  background: rgba(255,255,255,0.05);
  border-radius: var(--radius-lg);
  padding: 2rem;
}
.osfa-card h4 {
  color: var(--white);
  font-size: 1.05rem;
  margin-bottom: 0.65rem;
}
.osfa-card p {
  color: rgba(255,255,255,0.5);
  font-size: 0.93rem;
  line-height: 1.7;
  margin: 0;
}
.osfa-card-jeong {
  border: 1px solid rgba(26,111,184,0.5);
  background: rgba(10,79,138,0.15);
}
.osfa-card-jeong h4 { color: var(--primary-light); }
.osfa-card-jeong p { color: rgba(255,255,255,0.7); }
```

- [ ] **Step 3: Verify in browser**

Scroll past the trust bar — confirm:
- Dark section appears with headline "Most software is built for everyone..."
- Three cards visible: Generic SaaS, Stitched-Together Automations, The Jeong Way
- The Jeong Way card has a blue tinted border
- Text is readable (white/muted white on dark)

- [ ] **Step 4: Commit**

```bash
cd /c/Users/Derrick/ebygautomation && git add index.html css/styles.css && git commit -m "Add OSFA argument section — not one size fits all"
```

---

## Task 3: Replace Ecosystem Section with What We Build

**Files:**
- Modify: `index.html` — replace the entire `<!-- ECOSYSTEM INTRO -->` section (lines 175–203) with the What We Build section
- Modify: `css/styles.css` — add `.wwb-*` styles (ecosystem styles can stay for now — they'll stop being used)

- [ ] **Step 1: Replace ecosystem section in index.html**

Find and replace the entire ecosystem section — from `<!-- ========== ECOSYSTEM INTRO ========== -->` through its closing `</section>` — with:

```html
  <!-- ========== WHAT WE BUILD ========== -->
  <section class="what-we-build" id="what-we-build">
    <div class="container">
      <div class="section-center">
        <p class="section-tag">What We Build</p>
        <h2>Three disciplines. One <span class="highlight">relationship.</span></h2>
      </div>
      <div class="wwb-grid">
        <div class="wwb-card">
          <div class="wwb-num">01</div>
          <h3>AI Agents &amp; Automation</h3>
          <p>Custom AI agents and automated workflows embedded in your existing tools &mdash; email, CRM, documents, and project management. No ripping and replacing.</p>
          <div class="wwb-tags">
            <span class="wwb-tag">Workflow Automation</span>
            <span class="wwb-tag">AI Agents</span>
            <span class="wwb-tag">CRM Integration</span>
            <span class="wwb-tag">Document AI</span>
          </div>
        </div>
        <div class="wwb-card wwb-card-featured">
          <div class="wwb-num">02</div>
          <h3>Custom Software</h3>
          <p>Purpose-built applications &mdash; scheduling systems, client portals, internal tools, and dashboards &mdash; engineered around how your team actually works, not a generic template.</p>
          <div class="wwb-tags">
            <span class="wwb-tag">Web Applications</span>
            <span class="wwb-tag">Client Portals</span>
            <span class="wwb-tag">Internal Tools</span>
            <span class="wwb-tag">Dashboards</span>
          </div>
        </div>
        <div class="wwb-card">
          <div class="wwb-num">03</div>
          <h3>Professional Websites</h3>
          <p>Clean, fast, mobile-responsive websites built for performance and conversion &mdash; with ongoing management, security, and hosting included. One team, one relationship.</p>
          <div class="wwb-tags">
            <span class="wwb-tag">Design &amp; Development</span>
            <span class="wwb-tag">Hosting</span>
            <span class="wwb-tag">Ongoing Management</span>
          </div>
        </div>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Add What We Build CSS to styles.css**

After the closing brace of the `/* ---------- ABOUT ---------- */` block, insert:

```css
/* ---------- WHAT WE BUILD ---------- */
.what-we-build { padding: 6rem 0; }
.wwb-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}
.wwb-card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 2.5rem 2rem;
  transition: all var(--transition);
  display: flex;
  flex-direction: column;
}
.wwb-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-4px);
}
.wwb-card-featured {
  border-color: var(--primary);
  border-width: 2px;
}
.wwb-num {
  font-family: var(--font-heading);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--primary);
  margin-bottom: 0.75rem;
}
.wwb-card h3 { margin-bottom: 0.75rem; }
.wwb-card p {
  font-size: 0.95rem;
  color: var(--text-light);
  line-height: 1.65;
  margin-bottom: 1.5rem;
  flex-grow: 1;
}
.wwb-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: auto;
}
.wwb-tag {
  font-family: var(--font-heading);
  font-size: 0.68rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-light);
  background: var(--light);
  border: 1px solid var(--border);
  padding: 0.25rem 0.6rem;
  border-radius: 4px;
}
```

- [ ] **Step 3: Verify in browser**

Scroll to where the Ecosystem section used to be — confirm:
- "What We Build" section appears with three cards
- Custom Software card (02) has a blue border, others have grey
- Tags render as small pill labels at the bottom of each card
- "See What We Build" CTA in the hero now scrolls here correctly

- [ ] **Step 4: Commit**

```bash
cd /c/Users/Derrick/ebygautomation && git add index.html css/styles.css && git commit -m "Replace ecosystem section with What We Build — three disciplines"
```

---

## Task 4: Add Custom Software Deep-Dive Section

**Files:**
- Modify: `index.html` — insert new section immediately after the What We Build `</section>` closing tag
- Modify: `css/styles.css` — add `.custom-software` / `.cs-*` styles

- [ ] **Step 1: Insert Custom Software section into index.html**

Immediately after the closing `</section>` of the What We Build section, insert:

```html
  <!-- ========== CUSTOM SOFTWARE DEEP-DIVE ========== -->
  <section class="custom-software" id="custom-software">
    <div class="container">
      <div class="cs-inner">
        <div class="cs-content">
          <p class="section-tag cs-tag">Custom Software</p>
          <h2 class="cs-heading">When off-the-shelf doesn't fit,<br>we build the thing that does.</h2>
          <ul class="cs-list">
            <li>
              <h4>Scheduling &amp; Request Systems</h4>
              <p>Customer-facing booking portals with internal admin dashboards. Built for service businesses, research labs, and facilities management.</p>
            </li>
            <li>
              <h4>Client &amp; Vendor Portals</h4>
              <p>Secure, branded portals for document exchange, project tracking, and communication &mdash; replacing email chaos with structured workflows.</p>
            </li>
            <li>
              <h4>Internal Operations Tools</h4>
              <p>Custom dashboards, reporting systems, and workflow tools built around how your team actually operates &mdash; not how a SaaS vendor imagines you do.</p>
            </li>
            <li>
              <h4>AI-Integrated Applications</h4>
              <p>Custom software with AI built in &mdash; intelligent document processing, automated communication, and decision support from the ground up.</p>
            </li>
          </ul>
        </div>
        <div class="cs-callout">
          <h3>Technology second.<br>Always.</h3>
          <p>We never start with a platform or framework and look for problems it can solve. Every custom software engagement begins with operational mapping &mdash; understanding your workflows, your team, and your friction before any architecture decisions are made.</p>
          <p>The result is software that feels native to your business because it was built around it.</p>
          <a href="#contact" class="btn btn-outline cs-btn">Discuss Your Project</a>
        </div>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Add Custom Software CSS to styles.css**

After the closing brace of the `/* ---------- WHAT WE BUILD ---------- */` block, insert:

```css
/* ---------- CUSTOM SOFTWARE DEEP-DIVE ---------- */
.custom-software {
  padding: 6rem 0;
  background: var(--dark);
}
.cs-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}
.cs-tag { color: rgba(255,255,255,0.45) !important; }
.cs-heading {
  color: var(--white);
  margin-bottom: 2rem;
  line-height: 1.25;
}
.cs-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.cs-list li {
  background: rgba(255,255,255,0.05);
  border-radius: var(--radius);
  padding: 1.25rem;
}
.cs-list h4 {
  color: var(--white);
  font-size: 1rem;
  margin-bottom: 0.35rem;
}
.cs-list p {
  color: rgba(255,255,255,0.5);
  font-size: 0.88rem;
  line-height: 1.65;
  margin: 0;
}
.cs-callout {
  background: rgba(10,79,138,0.15);
  border: 1px solid rgba(26,111,184,0.4);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  position: sticky;
  top: calc(var(--header-h) + 2rem);
}
.cs-callout h3 {
  color: var(--white);
  font-size: 1.6rem;
  margin-bottom: 1.25rem;
  line-height: 1.3;
}
.cs-callout p {
  color: rgba(255,255,255,0.6);
  font-size: 0.93rem;
  line-height: 1.75;
  margin-bottom: 1rem;
}
.cs-btn {
  color: rgba(255,255,255,0.8) !important;
  border-color: rgba(255,255,255,0.3) !important;
  margin-top: 0.5rem;
}
.cs-btn:hover {
  background: var(--primary) !important;
  border-color: var(--primary) !important;
  color: var(--white) !important;
}
```

- [ ] **Step 3: Verify in browser**

Scroll past "What We Build" — confirm:
- Dark section appears immediately after
- Left column: "When off-the-shelf doesn't fit..." heading + 4 example type cards
- Right column: "Technology second. Always." callout box with blue tint
- "Discuss Your Project" button visible and links to #contact

- [ ] **Step 4: Commit**

```bash
cd /c/Users/Derrick/ebygautomation && git add index.html css/styles.css && git commit -m "Add Custom Software deep-dive section"
```

---

## Task 5: Replace Advantage Section with Closing Conviction

**Files:**
- Modify: `index.html` — replace the entire `<!-- COMPETITIVE ADVANTAGE -->` section with the Conviction section
- Modify: `css/styles.css` — add `.conviction` styles

- [ ] **Step 1: Replace advantage section in index.html**

Find and replace the entire advantage section — from `<!-- ========== COMPETITIVE ADVANTAGE ========== -->` through its closing `</section>` — with:

```html
  <!-- ========== CONVICTION ========== -->
  <section class="conviction">
    <div class="container">
      <div class="conviction-inner">
        <p class="section-tag">The Jeong AI Mission</p>
        <h2 class="conviction-statement">Quietly reliable.<br>Precisely yours.<br>Always there.<br><span class="highlight">That's &#51221;.</span></h2>
        <p class="conviction-sub">Software and AI systems built around how your business actually works &mdash; and a partnership that stays in place to make sure they keep working.</p>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Add Conviction CSS to styles.css**

Replace the entire `/* ---------- COMPETITIVE ADVANTAGE ---------- */` block with:

```css
/* ---------- CONVICTION ---------- */
.conviction {
  padding: 7rem 0;
  background: #f2ede3;
}
.conviction-inner {
  text-align: center;
  max-width: 640px;
  margin: 0 auto;
}
.conviction-statement {
  font-size: 2.6rem;
  line-height: 1.35;
  margin-bottom: 1.5rem;
  color: var(--dark);
}
.conviction-sub {
  font-size: 1.1rem;
  color: var(--text-light);
  line-height: 1.75;
  max-width: 520px;
  margin: 0 auto;
}
```

- [ ] **Step 3: Verify in browser**

Scroll to where the "Why Jeong AI" section used to be — confirm:
- Warm beige background section appears
- "The Jeong AI Mission" label
- "Quietly reliable. / Precisely yours. / Always there. / That's 정." — 정 rendered correctly
- No orphaned advantage section content

- [ ] **Step 4: Commit**

```bash
cd /c/Users/Derrick/ebygautomation && git add index.html css/styles.css && git commit -m "Replace advantage section with Conviction closing — that's 정"
```

---

## Task 6: Responsive CSS for New Sections

**Files:**
- Modify: `css/styles.css` — update all three responsive breakpoints

- [ ] **Step 1: Update 1024px breakpoint**

In the `@media (max-width: 1024px)` block, add after the existing `.ecosystem-brands` rule:

```css
  .osfa-grid { grid-template-columns: 1fr; }
  .wwb-grid { grid-template-columns: 1fr; max-width: 480px; margin: 0 auto; }
  .cs-inner { grid-template-columns: 1fr; }
  .cs-callout { position: static; }
```

- [ ] **Step 2: Update 768px breakpoint padding list**

In the `@media (max-width: 768px)` block, find the padding reduction rule:
```css
  .about, .friction, .ecosystem, .products, .services,
  .support, .how-it-works, .industries, .advantage,
  .cta-section, .web-services { padding: 4rem 0; }
```

Replace with:
```css
  .about, .friction, .osfa, .what-we-build, .custom-software,
  .products, .services, .support, .how-it-works, .industries,
  .conviction, .cta-section, .web-services { padding: 4rem 0; }
```

Then add after it:
```css
  .conviction-statement { font-size: 2rem; }
  .osfa-heading { font-size: 1.85rem; }
```

- [ ] **Step 3: Update 544px breakpoint padding list**

In the `@media (max-width: 544px)` block, find the padding reduction rule:
```css
  .about, .friction, .ecosystem, .products, .services,
  .support, .how-it-works, .industries, .advantage,
  .cta-section, .web-services { padding: 3rem 0; }
```

Replace with:
```css
  .about, .friction, .osfa, .what-we-build, .custom-software,
  .products, .services, .support, .how-it-works, .industries,
  .conviction, .cta-section, .web-services { padding: 3rem 0; }
```

Then add:
```css
  .conviction-statement { font-size: 1.7rem; }
  .osfa-heading { font-size: 1.5rem; }
  .cs-callout { padding: 1.75rem; }
```

- [ ] **Step 4: Verify responsive layouts**

In browser devtools, check at 768px width:
- OSFA cards stack to single column
- What We Build cards stack to single column
- Custom Software switches to single column (callout below examples)
- Conviction text scales down appropriately

- [ ] **Step 5: Commit**

```bash
cd /c/Users/Derrick/ebygautomation && git add css/styles.css && git commit -m "Add responsive CSS for new homepage sections"
```

---

## Task 7: Final Review Pass

**Files:**
- Modify: `index.html` — footer copyright fix + any remaining copy polish

- [ ] **Step 1: Fix footer copyright**

Find the footer line:
```html
<p>&copy; 2026 Jeong AI / Jeong AI. All rights reserved.</p>
```
Replace with:
```html
<p>&copy; 2026 Jeong AI. All rights reserved.</p>
```

- [ ] **Step 2: Full page walkthrough in browser**

Read through the full page at http://localhost:8080 and verify the narrative flow:
1. Hero: "Software Is Not One Size Fits All."
2. Trust bar: stats
3. OSFA: makes the argument (dark)
4. Philosophy: Jeong meaning
5. Problem: 4 friction areas
6. What We Build: 3 capabilities (light)
7. Custom Software: deep-dive (dark)
8. Products: $29–$149 (light)
9. Services: $2,500–$15,000
10. Support Plan
11. Web Services
12. How It Works
13. Industries
14. Conviction: "Quietly reliable. Precisely yours. Always there. That's 정." (warm beige)
15. CTA form

- [ ] **Step 3: Check anchor links**

Verify these all scroll correctly:
- Hero "See What We Build" → `#what-we-build`
- Hero "Book a Free Automation Audit" → `#contact`
- CS callout "Discuss Your Project" → `#contact`
- All nav links

- [ ] **Step 4: Final commit**

```bash
cd /c/Users/Derrick/ebygautomation && git add index.html && git commit -m "Final polish — footer fix and copy review"
```
