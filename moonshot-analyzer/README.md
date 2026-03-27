# Moonshot Analyzer

A systematic, 7-dimension scoring framework for evaluating high-risk/high-reward "moonshot" investment opportunities. Built as a Claude skill to identify and analyze companies riding structural megatrends with breakthrough technology and asymmetric risk/reward profiles.

## Overview

The Moonshot Analyzer uses a proprietary 100-point scoring system across 7 weighted dimensions to evaluate early-stage, high-growth companies that most traditional frameworks miss. It complements value investing approaches (like the Warren Buffett Analyst) by focusing specifically on pre-profit or early-growth companies positioned on structural megatrends.

### The 7 Dimensions

| # | Dimension | Weight | Core Question |
|---|-----------|--------|---------------|
| D1 | Megatrend & TAM | 20% | "How big is the wave?" |
| D2 | Technology & Breakthrough | 20% | "Is the innovation real?" |
| D3 | De-risking Progression | 15% | "Is risk declining?" |
| D4 | Asymmetric Risk/Reward | 15% | "Is the math in our favor?" |
| D5 | Growth Trajectory | 12% | "How fast, how scalable?" |
| D6 | Team & Execution | 8% | "Can these people deliver?" |
| D7 | Financial Runway & Burn | 10% | "Will the money last?" |

### Verdict Scale

| Score | Verdict | Suggested Position |
|-------|---------|-------------------|
| 80-100 | STRONG BUY CONVICTION | 2-3% of portfolio |
| 70-79 | HIGH CONVICTION WATCH | 1-2% of portfolio |
| 60-69 | SPECULATIVE WATCH | 0.5-1% of portfolio |
| 50-59 | MONITOR ONLY | 0% until catalysts |
| <50 | PASS | Avoid |

## Three Operating Modes

### Mode 1: Discovery Scan
Broad market sweep across **15 megatrend categories** to identify 15-25 candidates. Uses a 4-layer search methodology:

1. **Supply Chain Depth** — Look 2-3 layers deep in the supply chain
2. **Small Fish, Big Pond** — Micro/small-caps in massive TAMs
3. **Contra-Signal** — Stocks down 40-70% while fundamentals improve
4. **Capital Deployment** — Track insider buying, government grants, strategic investments

### Mode 2: Deep Dive
Full 100-point analysis of a single company with:
- Weighted sub-metric scoring for each dimension
- Knockout filters (penalties and bonuses)
- Bull/Base/Bear scenario table with probability weights
- Catalyst timeline (6-18 months)
- Position sizing recommendation

### Mode 3: Monitoring
Update existing scorecards with:
- Score delta tracking
- Catalyst status updates
- New development flags
- Action recommendations (HOLD / ADD / TRIM / EXIT)

## 15 Megatrend Categories

The framework scans across these structural megatrends:

| # | Megatrend | Example TAM (2030+) |
|---|-----------|-------------------|
| 1 | AI & Automation | $1.5-2T+ |
| 2 | Robotics & Autonomous Systems | $500B-1T |
| 3 | Autonomous Mobility & eVTOL | $400B-1T |
| 4 | Energy Transition | $2-3T+ |
| 5 | Next-Gen Connectivity | $300-500B |
| 6 | Space Economy | $600B-1T |
| 7 | Longevity & BioTech | $800B-1.5T |
| 8 | Multiomics & AI-Native Biology | $200-500B |
| 9 | Cybersecurity | $400-600B |
| 10 | Digital Finance & Blockchain | $500B-1T |
| 11 | Defense & Geopolitical Restructuring | $800B-1.5T |
| 12 | 3D Printing / Additive Manufacturing | $100-200B |
| 13 | Water, Food & Climate | $300-500B |
| 14 | Demographic Shift & Silver Economy | $2-4T+ |
| 15 | Quantum Computing | $50-100B |

## Installation & Setup

### Method 1: Claude Code (CLI) — Recommended

```bash
# 1. Clone the repo
git clone https://github.com/mertony8/claude-skills.git
cd claude-skills

# 2. Copy the skill to your Claude skills directory
cp -r moonshot-analyzer ~/.claude/skills/

# 3. Verify installation — the skill should appear when you start Claude Code
claude
```

After installation, Claude Code will automatically detect the skill via the `SKILL.md` frontmatter. You can verify by checking if "moonshot-analyzer" appears in your available skills.

### Method 2: Project-Level Installation

If you want the skill available only in a specific project:

```bash
# From your project root
mkdir -p .claude/skills
cp -r /path/to/moonshot-analyzer .claude/skills/
```

### Method 3: Direct Download

```bash
# Download just the skill files
mkdir -p ~/.claude/skills/moonshot-analyzer
curl -o ~/.claude/skills/moonshot-analyzer/SKILL.md \
  https://raw.githubusercontent.com/mertony8/claude-skills/main/moonshot-analyzer/SKILL.md

# Optional: download reference docs
mkdir -p ~/.claude/skills/moonshot-analyzer/references
curl -o ~/.claude/skills/moonshot-analyzer/references/scoring-methodology.md \
  https://raw.githubusercontent.com/mertony8/claude-skills/main/moonshot-analyzer/references/scoring-methodology.md
```

### Verifying Installation

Once installed, start a new Claude conversation and try:
```
Run a moonshot analysis on LUNR
```

If Claude responds with the 7-dimension scorecard format, the skill is working correctly. If not, check that `SKILL.md` is in the right directory and has valid YAML frontmatter.

### Requirements

| Requirement | Required? | Purpose |
|-------------|-----------|---------|
| Claude (Opus/Sonnet) | Yes | Core analysis engine |
| Web Search (`WebSearch`) | Recommended | Live stock data, news, earnings, analyst ratings |
| Web Fetch (`WebFetch`) | Recommended | SEC filings, press releases, detailed reports |
| File Write access | Optional | Save reports as `.md` files |
| Python (openpyxl) | Optional | Generate `.xlsx` dashboard exports |

The skill works without web tools if you provide financial data manually, but live data produces significantly better results.

---

## Configuration

The skill supports customization through natural language instructions. Tell Claude your preferences at the start of a conversation:

### Language
```
# Default: matches user's language (Turkish/English)
# Override:
Analyze RCAT in English
Tüm analizleri Türkçe yap
```

### Risk Tolerance
```
# Default: standard moonshot allocation (10-15% total portfolio)
# Conservative:
I'm conservative — cap moonshot positions at 0.5% each, 5% total
# Aggressive:
I'm comfortable with higher risk — allow up to 3% per position
```

### Output Format
```
# Default: full markdown report
# Compact:
Give me a compact scorecard only, skip the detailed analysis
# With spreadsheet:
Include a Google Sheets export row at the end
# Dashboard:
Generate an xlsx dashboard with all scores
```

### Focus Sectors
```
# Default: all 15 megatrends
# Filtered:
Only scan defense and space megatrends
Focus on AI infrastructure and quantum computing
Skip biotech and pharma
```

### Monitoring Frequency
```
# When using Mode 3:
Update my portfolio monthly — flag any score changes > 5 points
Only alert me on knockout filter triggers
```

---

## Usage — Step-by-Step Walkthroughs

### Walkthrough 1: Discovery Scan

**You say:**
```
Run a moonshot discovery scan. Focus on companies under $3B market cap
riding AI, defense, or space megatrends.
```

**What happens:**
1. Claude searches the web for current stock data across the specified megatrends
2. Applies the 4-layer search methodology (Supply Chain Depth, Small Fish Big Pond, Contra-Signal, Capital Deployment)
3. Scores each candidate on D1-D7 using the Quick Score (/35) system
4. Ranks and presents 15-25 candidates in a formatted table
5. Highlights multi-trend intersections, contra-signal opportunities, and insider buying signals
6. Recommends the top 10 for Deep Dive analysis

**Output:** A full report like [this example](./examples/discovery-scan-march-2026.md)

---

### Walkthrough 2: Deep Dive

**You say:**
```
Run a moonshot deep dive on RCAT (Red Cat Holdings)
```

**What happens:**
1. Claude gathers current data: stock price, market cap, financials, analyst ratings, insider activity, news
2. Scores all 7 dimensions with weighted sub-metrics (30+ individual data points)
3. Applies knockout filters (penalties and bonuses)
4. Builds Bull/Base/Bear scenario table with probability-weighted expected value
5. Maps upcoming catalysts on a 6-18 month timeline
6. Produces a Final Verdict with position sizing recommendation

**Output:** A complete scorecard like [this example](./examples/RCAT-deep-dive.md)

**Follow-up prompts you can use:**
```
Drill deeper into the Technology & Breakthrough dimension
How does RCAT compare to UMAC?
What's the biggest risk I should watch?
Generate a video script for this analysis
```

---

### Walkthrough 3: Monitoring Update

**You say:**
```
Update my RCAT moonshot scorecard. Last analysis was March 15 —
they just reported Q4 earnings and got a new DoD contract.
```

**What happens:**
1. Claude loads the previous scorecard context
2. Searches for all developments since the last analysis date
3. Re-scores affected dimensions and calculates score deltas
4. Updates catalyst status (hit/missed/delayed)
5. Checks for new knockout filter triggers
6. Recommends action: HOLD / ADD / TRIM / EXIT

**Output:**
```
RCAT Monitoring Update
Previous Score: 72/100 → Current Score: 75/100 (+3)

Catalyst Tracker:
  [HIT]     DoD SRR contract expansion — $50M additional
  [ON TRACK] DJI ban enforcement (Section 1709)
  [DELAYED]  International sales ramp — pushed to Q3

Score Deltas:
  D3 De-risking: 75 → 80 (+5) — new contract is major validation
  D7 Financial:  48 → 55 (+7) — Q4 revenue beat, cash improved

Action: HOLD — score trending up, no knockout triggers
```

---

### Walkthrough 4: Comparative Analysis

**You say:**
```
Compare RCAT vs UMAC vs LUNR as moonshot candidates.
Which one should I prioritize?
```

**What happens:**
1. Claude runs a quick deep dive on each ticker
2. Produces a side-by-side comparison table across all 7 dimensions
3. Highlights relative strengths and weaknesses
4. Recommends priority order based on risk-adjusted expected value

---

## Example Outputs

The `examples/` directory contains real analysis outputs produced by this skill:

| File | Type | Description |
|------|------|-------------|
| [`discovery-scan-march-2026.md`](./examples/discovery-scan-march-2026.md) | Discovery Scan | Full 15-megatrend scan with 25 candidates ranked by Quick Score |
| [`SKYT-deep-dive.md`](./examples/SKYT-deep-dive.md) | Deep Dive | SkyWater Technology — Score: 76/100, HIGH CONVICTION WATCH |
| [`RCAT-deep-dive.md`](./examples/RCAT-deep-dive.md) | Deep Dive | Red Cat Holdings — Score: 72/100, HIGH CONVICTION WATCH |
| [`NNE-deep-dive.md`](./examples/NNE-deep-dive.md) | Deep Dive | Nano Nuclear Energy — Aggressive Moonshot |
| [`moonshot-dashboard.xlsx`](./examples/moonshot-dashboard.xlsx) | Dashboard | Excel tracking spreadsheet with all scores and positions |

---

## Knockout Filters

The framework applies automatic adjustments after scoring:

### Penalties
| Filter | Condition | Impact |
|--------|-----------|--------|
| Breakthrough Overload | Needs >=3 unproven breakthroughs | -15 pts |
| Cash Crunch | <6 months runway, no funding | -20 pts |
| Insider Exodus | Major selling >20% in 6 months | -10 pts |
| Product Scatter | >5 unrelated product lines | -10 pts |
| Hype Peak | Peak hype cycle, max retail attention | -10 pts |

### Bonuses
| Filter | Condition | Impact |
|--------|-----------|--------|
| Trough Entry | Trough of disillusionment + improving fundamentals | +5 pts |
| Multi-Trend | 3+ megatrend intersection | +3 pts |
| De-risk Acceleration | Major de-risking event in last 3 months | +5 pts |

---

## Disclaimer

This framework is an analytical tool, **NOT investment advice**. Moonshot investments carry extreme risk including potential total loss of capital. The scores and verdicts are systematic assessments based on publicly available information and should not be the sole basis for any investment decision. Always do your own research and consult a qualified financial advisor before making investment decisions. Total moonshot allocation should stay under 10-15% of total portfolio.

## License

MIT License — see [LICENSE](../LICENSE) for details.

## Author

Built by [@mertony8](https://github.com/mertony8)
