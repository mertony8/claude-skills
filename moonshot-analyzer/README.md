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

## Installation

### Option 1: Claude Code (CLI)

Place the `moonshot-analyzer/` folder in your Claude skills directory:

```bash
# Clone the repo
git clone https://github.com/mertony8/claude-skills.git

# The skill will be automatically detected by Claude Code
```

### Option 2: Manual

1. Download the `SKILL.md` file
2. Place it in your Claude skills directory (`~/.claude/skills/moonshot-analyzer/SKILL.md`)
3. The skill will be available in your next conversation

## Usage Examples

### Discovery Scan
```
Run a moonshot discovery scan across all megatrends
```

### Deep Dive
```
Run a moonshot deep dive on RCAT (Red Cat Holdings)
```

### Monitoring
```
Update my SKYT moonshot scorecard with the latest Q4 earnings
```

## Example Outputs

The `examples/` directory contains real analysis outputs:

| File | Description |
|------|-------------|
| `discovery-scan-march-2026.md` | Full 15-megatrend discovery scan with 25 candidates |
| `SKYT-deep-dive.md` | SkyWater Technology deep dive (Score: 76/100) |
| `RCAT-deep-dive.md` | Red Cat Holdings deep dive (Score: 72/100) |
| `NNE-deep-dive.md` | Nano Nuclear Energy deep dive |

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

## Requirements

- **Claude** with web search capabilities (for live data gathering)
- Web search is used to pull current stock prices, earnings data, analyst ratings, and news
- Works without web search if the user provides data manually

## Disclaimer

This framework is an analytical tool, **NOT investment advice**. Moonshot investments carry extreme risk including potential total loss of capital. The scores and verdicts are systematic assessments based on publicly available information and should not be the sole basis for any investment decision. Always do your own research and consult a qualified financial advisor before making investment decisions. Total moonshot allocation should stay under 10-15% of total portfolio.

## License

MIT License — see [LICENSE](../LICENSE) for details.

## Author

Built by [@mertony8](https://github.com/mertony8)
