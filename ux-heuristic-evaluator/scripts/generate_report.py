"""
UX Heuristic Evaluation — PDF Report Generator

Usage:
  Save your evaluation data as JSON, then run:
    python generate_report.py evaluation_data.json output_report.pdf

The evaluation_data.json should follow this structure:
{
  "website_url": "https://example.com",
  "website_name": "Example Site",
  "evaluation_date": "2026-03-13",
  "pages_evaluated": [
    {"url": "https://example.com", "type": "Homepage"},
    {"url": "https://example.com/about", "type": "Content page"}
  ],
  "heuristics": [
    {
      "number": 1,
      "name": "Visibility of System Status",
      "rating": "Pass",
      "summary": "The site provides clear feedback...",
      "positives": ["Loading indicators on all async actions", "Clear active states in nav"],
      "issues": [
        {
          "description": "No confirmation message after contact form submission",
          "page": "https://example.com/contact",
          "severity": "Major"
        }
      ],
      "recommendations": ["Add a success message after form submission", "Add loading states to buttons"],
      "screenshots": [
        {
          "path": "/home/claude/evaluation_screenshots/h1_no_loading.png",
          "caption": "No loading indicator when applying filters — page appears frozen"
        }
      ]
    }
  ],
  "executive_summary": "Overall assessment paragraph...",
  "top_critical_issues": [
    "No form validation on the checkout page",
    "404 page has no navigation or search",
    "Mobile navigation is broken on product pages"
  ]
}

If you're calling this from within the skill workflow, Claude should:
1. Collect all findings into the JSON structure above
2. Write it to a temp file
3. Run this script to generate the PDF
4. Copy the PDF to /mnt/user-data/outputs/ and present it
"""

import json
import sys
import os
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, Image
)
from reportlab.platypus.flowables import Flowable


# ── Colors ──────────────────────────────────────────────────────────────────
COLOR_PASS = HexColor("#2E7D32")
COLOR_PARTIAL = HexColor("#F57F17")
COLOR_FAIL = HexColor("#C62828")
COLOR_PRIMARY = HexColor("#1565C0")
COLOR_DARK = HexColor("#212121")
COLOR_MUTED = HexColor("#616161")
COLOR_LIGHT_BG = HexColor("#F5F5F5")
COLOR_BORDER = HexColor("#E0E0E0")
COLOR_WHITE = white

SEVERITY_COLORS = {
    "Critical": HexColor("#C62828"),
    "Major": HexColor("#E65100"),
    "Minor": HexColor("#F57F17"),
    "Cosmetic": HexColor("#757575"),
}

RATING_COLORS = {
    "Pass": COLOR_PASS,
    "Partial": COLOR_PARTIAL,
    "Fail": COLOR_FAIL,
}


# ── Custom Flowables ────────────────────────────────────────────────────────
class RatingBadge(Flowable):
    """A colored badge showing Pass/Partial/Fail."""
    def __init__(self, rating, width=60, height=20):
        Flowable.__init__(self)
        self.rating = rating
        self.width = width
        self.height = height

    def draw(self):
        color = RATING_COLORS.get(self.rating, COLOR_MUTED)
        self.canv.setFillColor(color)
        self.canv.roundRect(0, 0, self.width, self.height, 3, fill=1, stroke=0)
        self.canv.setFillColor(COLOR_WHITE)
        self.canv.setFont("Helvetica-Bold", 9)
        text_width = self.canv.stringWidth(self.rating, "Helvetica-Bold", 9)
        self.canv.drawString((self.width - text_width) / 2, 6, self.rating)


class SeverityDot(Flowable):
    """A small colored dot for severity indication."""
    def __init__(self, severity, size=8):
        Flowable.__init__(self)
        self.severity = severity
        self.width = size
        self.height = size

    def draw(self):
        color = SEVERITY_COLORS.get(self.severity, COLOR_MUTED)
        self.canv.setFillColor(color)
        self.canv.circle(self.width / 2, self.height / 2, self.width / 2, fill=1, stroke=0)


# ── Styles ──────────────────────────────────────────────────────────────────
def get_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'CoverTitle', parent=styles['Title'],
        fontSize=28, leading=34, textColor=COLOR_PRIMARY,
        spaceAfter=8, alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'CoverSubtitle', parent=styles['Normal'],
        fontSize=14, leading=18, textColor=COLOR_MUTED,
        spaceAfter=4, alignment=TA_CENTER
    ))
    styles.add(ParagraphStyle(
        'SectionHeading', parent=styles['Heading1'],
        fontSize=18, leading=22, textColor=COLOR_PRIMARY,
        spaceBefore=20, spaceAfter=10,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'HeuristicHeading', parent=styles['Heading2'],
        fontSize=14, leading=18, textColor=COLOR_DARK,
        spaceBefore=14, spaceAfter=6,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'SubHeading', parent=styles['Heading3'],
        fontSize=11, leading=14, textColor=COLOR_DARK,
        spaceBefore=8, spaceAfter=4,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'Body', parent=styles['Normal'],
        fontSize=10, leading=14, textColor=COLOR_DARK,
        spaceAfter=6, alignment=TA_JUSTIFY
    ))
    styles.add(ParagraphStyle(
        'BulletText', parent=styles['Normal'],
        fontSize=10, leading=14, textColor=COLOR_DARK,
        leftIndent=15, spaceAfter=3
    ))
    styles.add(ParagraphStyle(
        'SmallMuted', parent=styles['Normal'],
        fontSize=8, leading=10, textColor=COLOR_MUTED,
        alignment=TA_CENTER
    ))
    styles.add(ParagraphStyle(
        'TableCell', parent=styles['Normal'],
        fontSize=9, leading=12, textColor=COLOR_DARK,
    ))
    styles.add(ParagraphStyle(
        'TableHeader', parent=styles['Normal'],
        fontSize=9, leading=12, textColor=COLOR_WHITE,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'CaptionText', parent=styles['Normal'],
        fontSize=8, leading=11, textColor=COLOR_MUTED,
        spaceAfter=8, alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    ))

    return styles


# ── Report Builder ──────────────────────────────────────────────────────────
def build_report(data, output_path):
    styles = get_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2.5 * cm, bottomMargin=2 * cm
    )

    story = []

    # ── Cover Page ──────────────────────────────────────────────────────
    story.append(Spacer(1, 80))
    story.append(Paragraph("Usability Heuristic<br/>Evaluation", styles['CoverTitle']))
    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="40%", thickness=2, color=COLOR_PRIMARY))
    story.append(Spacer(1, 16))
    story.append(Paragraph(data.get("website_name", "Website"), styles['CoverSubtitle']))
    story.append(Paragraph(data.get("website_url", ""), styles['CoverSubtitle']))
    story.append(Spacer(1, 24))
    story.append(Paragraph(
        f"Evaluation Date: {data.get('evaluation_date', datetime.now().strftime('%Y-%m-%d'))}",
        styles['CoverSubtitle']
    ))
    story.append(Paragraph("Evaluator: AI-Assisted UX Audit (Claude)", styles['CoverSubtitle']))
    story.append(Spacer(1, 40))
    story.append(Paragraph(
        "Based on Jakob Nielsen's 10 Usability Heuristics for User Interface Design",
        styles['SmallMuted']
    ))
    story.append(PageBreak())

    # ── Executive Summary ───────────────────────────────────────────────
    story.append(Paragraph("Executive Summary", styles['SectionHeading']))
    story.append(Paragraph(data.get("executive_summary", ""), styles['Body']))
    story.append(Spacer(1, 12))

    # Quick-reference ratings table
    heuristics = data.get("heuristics", [])
    ratings_data = [
        [
            Paragraph("<b>#</b>", styles['TableHeader']),
            Paragraph("<b>Heuristic</b>", styles['TableHeader']),
            Paragraph("<b>Rating</b>", styles['TableHeader']),
        ]
    ]
    pass_count = partial_count = fail_count = 0
    for h in heuristics:
        rating = h.get("rating", "N/A")
        if rating == "Pass": pass_count += 1
        elif rating == "Partial": partial_count += 1
        elif rating == "Fail": fail_count += 1

        color = RATING_COLORS.get(rating, COLOR_MUTED)
        ratings_data.append([
            Paragraph(str(h.get("number", "")), styles['TableCell']),
            Paragraph(h.get("name", ""), styles['TableCell']),
            Paragraph(f'<font color="{color.hexval()}">{rating}</font>', styles['TableCell']),
        ])

    col_widths = [30, 340, 80]
    ratings_table = Table(ratings_data, colWidths=col_widths)
    ratings_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_WHITE),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_WHITE, COLOR_LIGHT_BG]),
    ]))
    story.append(ratings_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        f"<b>Summary:</b> {pass_count} Pass &nbsp;|&nbsp; {partial_count} Partial &nbsp;|&nbsp; {fail_count} Fail",
        styles['Body']
    ))
    story.append(Spacer(1, 10))

    # Top critical issues
    top_issues = data.get("top_critical_issues", [])
    if top_issues:
        story.append(Paragraph("<b>Top Critical Issues:</b>", styles['SubHeading']))
        for i, issue in enumerate(top_issues, 1):
            story.append(Paragraph(f"{i}. {issue}", styles['BulletText']))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ── Methodology ─────────────────────────────────────────────────────
    story.append(Paragraph("Methodology", styles['SectionHeading']))
    story.append(Paragraph(
        "This evaluation was conducted using Jakob Nielsen's 10 Usability Heuristics "
        "for User Interface Design, a widely recognized framework for identifying "
        "usability issues in digital interfaces. The evaluation involved crawling "
        "multiple pages of the website and systematically assessing each page against "
        "all 10 heuristics.",
        styles['Body']
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Each heuristic is rated as <b>Pass</b> (meets the heuristic well), "
        "<b>Partial</b> (mixed compliance with notable gaps), or "
        "<b>Fail</b> (significant violations observed). Individual issues are "
        "rated by severity: Critical, Major, Minor, or Cosmetic.",
        styles['Body']
    ))
    story.append(Spacer(1, 10))

    # Pages evaluated
    pages = data.get("pages_evaluated", [])
    if pages:
        story.append(Paragraph("<b>Pages Evaluated:</b>", styles['SubHeading']))
        pages_data = [
            [
                Paragraph("<b>Page Type</b>", styles['TableHeader']),
                Paragraph("<b>URL</b>", styles['TableHeader']),
            ]
        ]
        for p in pages:
            pages_data.append([
                Paragraph(p.get("type", ""), styles['TableCell']),
                Paragraph(p.get("url", ""), styles['TableCell']),
            ])

        pages_table = Table(pages_data, colWidths=[120, 330])
        pages_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
            ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_WHITE),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_WHITE, COLOR_LIGHT_BG]),
        ]))
        story.append(pages_table)

    story.append(PageBreak())

    # ── Detailed Findings ───────────────────────────────────────────────
    story.append(Paragraph("Detailed Findings", styles['SectionHeading']))

    for h in heuristics:
        number = h.get("number", "")
        name = h.get("name", "")
        rating = h.get("rating", "N/A")
        summary = h.get("summary", "")
        positives = h.get("positives", [])
        issues = h.get("issues", [])
        recommendations = h.get("recommendations", [])

        rating_color = RATING_COLORS.get(rating, COLOR_MUTED)

        # Heuristic header with rating
        section_items = []
        section_items.append(Paragraph(
            f'#{number}: {name} &nbsp;&nbsp;'
            f'<font color="{rating_color.hexval()}"><b>[{rating}]</b></font>',
            styles['HeuristicHeading']
        ))
        section_items.append(Paragraph(summary, styles['Body']))

        # Screenshots
        screenshots = h.get("screenshots", [])
        for ss in screenshots:
            img_path = ss.get("path", "")
            caption = ss.get("caption", "")
            if img_path and os.path.exists(img_path):
                try:
                    # Calculate image dimensions to fit within page width
                    max_width = 450
                    max_height = 250
                    img = Image(img_path)
                    iw, ih = img.imageWidth, img.imageHeight
                    if iw > 0 and ih > 0:
                        ratio = min(max_width / iw, max_height / ih)
                        img = Image(img_path, width=iw * ratio, height=ih * ratio)
                    else:
                        img = Image(img_path, width=max_width, height=max_height)
                    section_items.append(Spacer(1, 6))
                    section_items.append(img)
                    if caption:
                        section_items.append(Paragraph(caption, styles['CaptionText']))
                    section_items.append(Spacer(1, 4))
                except Exception as e:
                    section_items.append(Paragraph(
                        f"<i>[Screenshot: {caption or img_path} — could not embed: {e}]</i>",
                        styles['CaptionText']
                    ))

        # Positives
        if positives:
            section_items.append(Paragraph("<b>What works well:</b>", styles['SubHeading']))
            for pos in positives:
                section_items.append(Paragraph(f"\u2022 {pos}", styles['BulletText']))

        # Issues
        if issues:
            section_items.append(Spacer(1, 4))
            section_items.append(Paragraph("<b>Issues Found:</b>", styles['SubHeading']))

            issues_data = [
                [
                    Paragraph("<b>Issue</b>", styles['TableHeader']),
                    Paragraph("<b>Page</b>", styles['TableHeader']),
                    Paragraph("<b>Severity</b>", styles['TableHeader']),
                ]
            ]
            for issue in issues:
                sev = issue.get("severity", "Minor")
                sev_color = SEVERITY_COLORS.get(sev, COLOR_MUTED)
                issues_data.append([
                    Paragraph(issue.get("description", ""), styles['TableCell']),
                    Paragraph(issue.get("page", ""), styles['TableCell']),
                    Paragraph(f'<font color="{sev_color.hexval()}">{sev}</font>', styles['TableCell']),
                ])

            issues_table = Table(issues_data, colWidths=[240, 140, 70])
            issues_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
                ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_WHITE),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_WHITE, COLOR_LIGHT_BG]),
            ]))
            section_items.append(issues_table)

        # Recommendations
        if recommendations:
            section_items.append(Spacer(1, 4))
            section_items.append(Paragraph("<b>Recommendations:</b>", styles['SubHeading']))
            for rec in recommendations:
                section_items.append(Paragraph(f"\u2022 {rec}", styles['BulletText']))

        section_items.append(Spacer(1, 8))
        section_items.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER))

        story.append(KeepTogether(section_items[:3]))  # Keep header + summary together
        story.extend(section_items[3:])

    story.append(PageBreak())

    # ── Priority Matrix ─────────────────────────────────────────────────
    story.append(Paragraph("Priority Matrix", styles['SectionHeading']))
    story.append(Paragraph(
        "All issues consolidated and ranked by severity to guide remediation efforts.",
        styles['Body']
    ))
    story.append(Spacer(1, 8))

    # Gather all issues across heuristics
    all_issues = []
    for h in heuristics:
        for issue in h.get("issues", []):
            all_issues.append({
                "heuristic": f"#{h.get('number', '')} {h.get('name', '')}",
                **issue
            })

    severity_order = {"Critical": 0, "Major": 1, "Minor": 2, "Cosmetic": 3}
    all_issues.sort(key=lambda x: severity_order.get(x.get("severity", "Minor"), 99))

    if all_issues:
        matrix_data = [
            [
                Paragraph("<b>Severity</b>", styles['TableHeader']),
                Paragraph("<b>Issue</b>", styles['TableHeader']),
                Paragraph("<b>Heuristic</b>", styles['TableHeader']),
            ]
        ]
        for issue in all_issues:
            sev = issue.get("severity", "Minor")
            sev_color = SEVERITY_COLORS.get(sev, COLOR_MUTED)
            matrix_data.append([
                Paragraph(f'<font color="{sev_color.hexval()}">{sev}</font>', styles['TableCell']),
                Paragraph(issue.get("description", ""), styles['TableCell']),
                Paragraph(issue.get("heuristic", ""), styles['TableCell']),
            ])

        matrix_table = Table(matrix_data, colWidths=[65, 235, 150])
        matrix_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
            ('TEXTCOLOR', (0, 0), (-1, 0), COLOR_WHITE),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_WHITE, COLOR_LIGHT_BG]),
        ]))
        story.append(matrix_table)
    else:
        story.append(Paragraph("No issues found — excellent usability!", styles['Body']))

    # ── Build ───────────────────────────────────────────────────────────
    doc.build(story)
    print(f"Report generated: {output_path}")


# ── CLI entry point ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_report.py <evaluation_data.json> <output.pdf>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r") as f:
        data = json.load(f)

    build_report(data, output_path)
