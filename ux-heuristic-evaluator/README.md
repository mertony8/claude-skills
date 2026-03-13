# UX Heuristic Evaluator

Evaluate any website's usability against **Jakob Nielsen's 10 Usability Heuristics**, producing a professional PDF audit report with Pass / Partial / Fail ratings, evidence-based findings, and actionable recommendations.

## What It Does

Given a website URL, this skill:

1. **Asks the user** whether to evaluate the full site or just a single page
2. **Crawls the site** using Claude in Chrome — visiting up to 8-12 key pages (homepage, forms, content pages, error pages, help sections)
3. **Inspects each page** for accessibility, navigation, consistency, error handling, and more
4. **Evaluates against all 10 heuristics** with specific evidence and severity-rated issues
5. **Generates a professional PDF report** with executive summary, per-heuristic findings, and a priority matrix

## Sample Output

See the [examples/](./examples/) folder for real evaluation reports:

| Site | Type | Score | Highlights |
|------|------|-------|------------|
| [CoinDive](./examples/coindive-ux-heuristic-evaluation.pdf) | Crypto data platform | 7 Pass, 2 Partial, 1 Fail | Excellent system status, blank 404 page |
| [Wikipedia](./examples/wikipedia-ux-heuristic-evaluation.pdf) | Encyclopedia portal | 5 Pass, 4 Partial, 0 Fail | Functional minimalism, accessibility gaps |
| [Notion (Marketing)](./examples/notion-marketing-ux-heuristic-evaluation.pdf) | SaaS homepage | 8 Pass, 2 Partial, 0 Fail | Enterprise-grade UX, 49% images lack alt text |
| [Notion (App)](./examples/notion-app-ux-heuristic-evaluation.pdf) | Productivity app (logged in) | 9 Pass, 1 Partial, 0 Fail | Near-perfect scores, minor accessibility gaps |

The generated PDF includes:

- **Cover page** with site name, URL, and evaluation date
- **Executive summary** with quick-reference ratings table
- **Detailed findings** for each of the 10 heuristics (rating, positives, issues, recommendations)
- **Priority matrix** ranking all issues by severity (Critical → Cosmetic)

## The 10 Heuristics Evaluated

| # | Heuristic | What It Checks |
|---|-----------|---------------|
| 1 | Visibility of System Status | Loading indicators, active nav states, feedback |
| 2 | Match Between System and Real World | Language, conventions, information order |
| 3 | User Control and Freedom | Undo, cancel, back navigation, exit paths |
| 4 | Consistency and Standards | Visual consistency, terminology, conventions |
| 5 | Error Prevention | Input validation, confirmations, constraints |
| 6 | Recognition Rather Than Recall | Visible navigation, labels, contextual info |
| 7 | Flexibility and Efficiency of Use | Search, shortcuts, skip links, filters |
| 8 | Aesthetic and Minimalist Design | Visual hierarchy, whitespace, focus |
| 9 | Help Users Recover from Errors | Error messages, 404 pages, recovery paths |
| 10 | Help and Documentation | FAQ, contextual help, contact options |

## Requirements

- **Claude in Chrome** — browser extension for site crawling
- **Computer Use** enabled — for Python/reportlab PDF generation
- Python packages: `reportlab` (pre-installed in Claude's environment)

## Usage

Upload the `.skill` file to Claude, then prompt:

```
Evaluate the usability of https://example.com
```

or

```
Run a heuristic evaluation on https://example.com
```

Claude will ask whether you want a full site or single page evaluation, then proceed with the audit.

## File Structure

```
ux-heuristic-evaluator/
├── SKILL.md                    ← Main skill instructions (5 phases)
├── references/
│   └── heuristics.md           ← Detailed definitions for all 10 heuristics
└── scripts/
    └── generate_report.py      ← PDF report generator (reportlab)
```

## Rating Scale

| Rating | Meaning |
|--------|---------|
| **Pass** | Meets the heuristic well across all or nearly all observed pages |
| **Partial** | Mixed compliance with notable gaps or inconsistencies |
| **Fail** | Significant violations causing user confusion or task failure |

## Issue Severity

| Severity | Priority |
|----------|----------|
| **Critical** | Prevents core task completion — fix immediately |
| **Major** | Causes significant confusion — high priority |
| **Minor** | Noticeable friction, users can work around it |
| **Cosmetic** | Polish issue — low priority |

## Known Limitations

- **No screenshot embedding in PDF (yet):** Browser screenshots are captured during the crawl and serve as visual evidence for the evaluator, but cannot currently be saved to the filesystem for PDF embedding. The `generate_report.py` script already supports image embedding — this will be activated when the platform adds a `save_screenshot_to_disk` capability.
- **html2canvas compatibility:** Some sites using modern CSS features (e.g., `lab()`, `oklch()` color functions) are incompatible with the html2canvas library used for alternative screenshot capture.
- **Logged-in evaluations:** The skill can evaluate authenticated app experiences (e.g., Notion, Figma) when the user is already logged in. Navigate to the app in the browser first, then trigger the evaluation.

## Roadmap

- [ ] Screenshot embedding in PDF reports
- [ ] Mobile viewport evaluation mode
- [ ] Automated WCAG accessibility checks alongside heuristic evaluation
- [ ] Comparison mode (evaluate two versions of the same site)

