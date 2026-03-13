---
name: ux-heuristic-evaluator
description: Evaluate any website's usability against Jakob Nielsen's 10 Usability Heuristics. Use this skill whenever the user wants a UX audit, heuristic evaluation, usability review, or expert review of a website. Triggers include phrases like "evaluate this website", "UX audit", "heuristic evaluation", "usability review", "check the usability of", "Nielsen heuristics", "expert review", or any request to assess a site's user experience quality. Also trigger when the user shares a URL and asks about its design quality, UX issues, or usability problems — even if they don't explicitly mention "heuristics". This skill requires Claude in Chrome (browser tools) to crawl and inspect the website.
---

# UX Heuristic Evaluator

Evaluate websites against Jakob Nielsen's 10 Usability Heuristics, producing a professional PDF audit report with Pass / Partial / Fail ratings, evidence-based findings, and actionable recommendations.

## Prerequisites

This skill requires **Claude in Chrome** (browser automation tools). Before starting, confirm you have access to:
- `tabs_context_mcp` (to get active tab)
- `navigate` (to visit URLs)
- `read_page` (to inspect page structure / accessibility tree)
- `get_page_text` (to extract page content)
- `computer` with `screenshot` action (to capture visual evidence)
- `javascript_tool` (to extract links, check interactive elements)
- `find` (to locate specific UI elements)

Also requires access to the **computer environment** for PDF generation via Python (reportlab).

If Claude in Chrome is not available, inform the user that this skill needs browser tools enabled and offer to do a limited evaluation based on screenshots the user provides manually.

## Workflow Overview

The evaluation follows 5 phases:

```
Phase 0: Scope Selection  →  Phase 1: Discovery & Crawl  →  Phase 2: Page-Level Inspection  →  Phase 3: Heuristic Evaluation  →  Phase 4: Report Generation
```

---

## Phase 0: Scope Selection

**Before doing anything else, ask the user how they want the evaluation scoped.** Present two options:

1. **Full site evaluation** — Crawl the homepage and up to 8-12 key internal pages (navigation destinations, forms, content pages, error pages, help pages). This gives the most comprehensive assessment across all 10 heuristics.
2. **Single page evaluation** — Evaluate only the specific URL provided. Useful for targeted audits of a specific page, a new design, or a landing page. Some heuristics (like Consistency and Standards) will be evaluated with limited evidence since cross-page comparison isn't possible.

Use the `ask_user_input` tool to present this choice (if available), or ask the question in prose.

Once the user has chosen, proceed accordingly:
- **Full site** → Follow Phase 1 as written below (discover links, prioritize pages, crawl multiple pages).
- **Single page** → Skip Steps 1.2 and 1.3, and only perform Step 1.1 and 1.4 on the given URL. In Phase 2, perform all inspections on the single page only. In Phase 3, note which heuristics have limited evidence due to single-page scope (especially #4 Consistency and Standards, and #7 Flexibility and Efficiency).

---

## Phase 1: Discovery & Crawl

The goal is to build a representative map of the website. A full crawl means visiting as many meaningful, distinct pages as feasible — not every URL on the internet.

**If the user chose "Single page" in Phase 0, skip Steps 1.2 and 1.3 — go directly to Step 1.4 for the provided URL only.**

### Step 1.1 — Start from the provided URL

1. Use `tabs_context_mcp` to get your active tab ID.
2. Navigate to the user's URL using `navigate`.
3. Take a screenshot to confirm the page loaded.
4. Use `get_page_text` to extract the page content.
5. Use `read_page` (filter: "all") to get the page structure.

### Step 1.2 — Discover internal links

Use `javascript_tool` to extract all internal links from the page:

```javascript
// Extract unique internal links from the current page
(() => {
  const base = new URL(window.location.href);
  const links = [...document.querySelectorAll('a[href]')]
    .map(a => {
      try { return new URL(a.href, base).href; } catch { return null; }
    })
    .filter(href => href && new URL(href).hostname === base.hostname)
    .filter(href => !href.match(/\.(pdf|zip|png|jpg|jpeg|gif|svg|mp4|mp3|css|js)(\?|$)/i))
    .filter(href => !href.includes('#'));
  return [...new Set(links)].slice(0, 50);
})()
```

### Step 1.3 — Prioritize pages to visit

From the discovered links, prioritize pages that give the best coverage for a heuristic evaluation. Aim for **up to 8-12 pages** (adjust based on site size). Prioritize in this order:

1. **Homepage** (already visited)
2. **Primary navigation destinations** — main menu items, top-level sections
3. **A form or input page** — contact, signup, search, checkout — critical for error prevention and user control heuristics
4. **A content/detail page** — article, product detail, service page — tests information architecture and readability
5. **Help/FAQ/Documentation page** — directly relevant to Heuristic #10
6. **An interactive feature** — filters, search results, dashboard — tests flexibility, efficiency, system status
7. **Error/404 page** — try navigating to a non-existent path like `/this-page-does-not-exist-404-test`
8. **Secondary/deeper pages** — fill remaining slots with pages that look structurally different

If the site is small (fewer than 8 distinct pages), visit all of them.

### Step 1.4 — Visit each prioritized page

For each page, collect:
- **Screenshot** (via `computer` → `screenshot`) — take a screenshot of each page for visual reference during the evaluation. These are visible in the conversation and serve as evidence for your findings.
- **Page text** (via `get_page_text`)
- **Interactive elements** (via `read_page` with filter: "interactive")
- **Full accessibility tree** (via `read_page` with filter: "all", depth: 5)

**About screenshots in the report:**

Screenshots taken with the `computer screenshot` tool are visible to you (the evaluator) during the crawl and serve as the visual evidence base for your findings. However, due to current platform limitations, these screenshots cannot be directly embedded into the generated PDF report. The report relies on detailed textual descriptions of visual findings instead.

If screenshot embedding becomes available in the future (e.g., via a `save_screenshot_to_disk` capability), the `generate_report.py` script already supports embedding images — simply add a `screenshots` array to each heuristic in the evaluation JSON with `path` and `caption` fields.

Store observations mentally as you go — you'll need them in Phase 3. Keep a running list of pages visited with their URLs and what type of page they are.

---

## Phase 2: Page-Level Inspection

While visiting pages in Phase 1, also perform these targeted checks. These directly feed into the heuristic evaluation.

### 2.1 — System Status Signals
Look for: loading indicators, progress bars, active/selected states in navigation, breadcrumbs, confirmation messages after actions. Check if the page gives any feedback when you interact with elements.

### 2.2 — Language & Conventions
Check: Is the language user-facing or jargon-heavy? Are icons recognizable? Does the information hierarchy follow real-world logic (e.g., dates, currencies, units)?

### 2.3 — Navigation & Control
Check: Is there a visible way to go back? Can users undo actions? Is the main navigation persistent and accessible? Are there dead ends?

### 2.4 — Consistency Audit
Compare across pages: Are fonts, colors, button styles, and spacing consistent? Does the header/footer change? Are similar actions labeled the same way throughout?

### 2.5 — Error Prevention & Handling
If forms exist: Are required fields marked? Are there input constraints (date pickers, dropdowns vs free text)? Try to find error states if possible. Visit the 404 page to check error messaging.

### 2.6 — Recognition vs Recall
Check: Are labels visible on form fields (not just placeholders)? Is navigation visible or hidden behind hamburger menus on desktop? Are there tooltips or contextual help?

### 2.7 — Flexibility & Efficiency
Look for: keyboard shortcuts, search functionality, filters, breadcrumbs, skip links. Check if the site offers different paths to the same content.

### 2.8 — Visual Design & Minimalism
Assess: Is the layout cluttered or focused? Is there visual hierarchy? Does every element serve a purpose? Is there excessive decoration competing with content?

### 2.9 — Error Messages
If you find any error states (404, form validation, etc.), check: Are messages in plain language? Do they explain what went wrong? Do they suggest next steps?

### 2.10 — Help & Documentation
Check: Is there a help section, FAQ, or documentation? Is it searchable? Is contextual help available (tooltips, inline guidance)? Is help easy to find from anywhere on the site?

---

## Phase 3: Heuristic Evaluation

Now synthesize your observations into a structured evaluation. For each of the 10 heuristics, determine a rating and document your findings.

Read the detailed heuristic definitions from `references/heuristics.md` before scoring.

### Rating Scale

| Rating | Meaning | Criteria |
|--------|---------|----------|
| **Pass** | Meets the heuristic well | The site demonstrates clear, consistent adherence to this principle across all or nearly all observed pages. Minor imperfections may exist but don't meaningfully impact usability. |
| **Partial** | Mixed compliance | The site meets this heuristic in some areas but has notable gaps or inconsistencies. Users may encounter friction in specific flows or pages. |
| **Fail** | Significant violations | The site clearly violates this heuristic in ways that would cause user confusion, frustration, or task failure. Multiple or severe issues observed. |

### For each heuristic, document:

1. **Rating**: Pass / Partial / Fail
2. **Summary**: 1-2 sentence overall assessment
3. **Positive findings**: What the site does well (even if the overall rating is Fail, acknowledge strengths)
4. **Issues found**: Specific problems observed, with the page URL and description
5. **Severity per issue**: Cosmetic / Minor / Major / Critical
6. **Recommendations**: Concrete, actionable fixes — not vague advice
7. **Screenshots**: Select 1-2 key screenshots per heuristic that best illustrate the finding. For each screenshot, provide:
   - The screenshot ID (from Phase 1)
   - A brief caption explaining what the screenshot shows and why it's relevant to this heuristic

**Screenshot selection strategy:** Choose screenshots that serve as visual evidence — a blank 404 page for Heuristic #9, a cluttered layout for #8, missing active nav state for #1, etc. Prioritize screenshots that show issues over screenshots that show things working well (unless the heuristic is Pass and you want to highlight good UX). Not every heuristic needs a screenshot — skip it if no visual evidence adds value.

After selecting screenshots, save them to the working directory. Use `upload_image` or copy the screenshot files so they are available at known file paths for the PDF generator:

```
/home/claude/evaluation_screenshots/
├── h1_system_status.png
├── h4_consistency_issue.png
├── h9_404_page.png
└── ...
```

### Issue Severity Definitions

- **Critical**: Prevents users from completing core tasks. Must fix immediately.
- **Major**: Causes significant confusion or frustration. High priority fix.
- **Minor**: Noticeable friction but users can work around it. Medium priority.
- **Cosmetic**: Polish issue. Low priority but improves perceived quality.

---

## Phase 4: Report Generation

Generate a professional PDF audit report using the Python script at `scripts/generate_report.py`. Read that file and follow its instructions for generating the report.

If the script is not available, generate the PDF using reportlab directly following the structure below.

### Report Structure

The PDF should include these sections:

1. **Cover Page**
   - Title: "Usability Heuristic Evaluation"
   - Subtitle: Website name and URL
   - Date of evaluation
   - Evaluator: "AI-Assisted UX Audit (Claude)"

2. **Executive Summary**
   - Overall usability assessment (1 paragraph)
   - Quick-reference table: all 10 heuristics with their Pass/Partial/Fail rating
   - Total counts: X Pass, Y Partial, Z Fail
   - Top 3 most critical issues (one sentence each)

3. **Methodology**
   - Brief note: Nielsen's 10 Usability Heuristics framework
   - Pages evaluated (list with URLs)
   - Rating scale explanation

4. **Detailed Findings** (one section per heuristic)
   - Heuristic number, name, and rating badge
   - Definition (one sentence from Nielsen)
   - Summary of findings
   - **Key screenshot(s)** — 1-2 embedded images with captions illustrating the most important finding for this heuristic
   - Positive observations
   - Issues table: Issue description | Page | Severity
   - Recommendations

5. **Summary & Priority Matrix**
   - All issues ranked by severity
   - Suggested fix priorities: Quick wins, medium-term, long-term

6. **Appendix**
   - List of all pages crawled with URLs

### PDF Styling Guidelines

Use the PDF skill (reportlab) to create a polished document:
- Use a clean sans-serif feel (Helvetica)
- Color-code ratings: Pass = green (#2E7D32), Partial = amber (#F57F17), Fail = red (#C62828)
- Use tables for structured data
- Keep it professional — this is a deliverable someone would share with stakeholders

---

## Important Notes

- **Be specific, not generic.** Every finding should reference a specific page, element, or behavior you actually observed. Never say "the site could improve X" without pointing to where.
- **Be balanced.** Even sites with poor usability do some things right. Acknowledge what works. This builds credibility and makes the report more actionable.
- **Context matters.** A complex B2B enterprise app has different expectations than a landing page. Calibrate your assessment to the site's purpose and audience.
- **Screenshots are evidence.** Take screenshots of both good examples and issues. Reference them in findings when possible.
- **Don't invent issues.** Only report what you actually observed during the crawl. If you couldn't test something (e.g., no forms on the site), note it as "Not evaluated" rather than speculating.
