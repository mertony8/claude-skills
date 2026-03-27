---
name: moonshot-analyzer
description: "7-dimension moonshot stock scoring framework for companies riding megatrends with breakthrough tech and asymmetric risk/reward. Use when analyzing moonshot stocks, disruptive companies, 10x opportunities, or running discovery scans. Trigger on \"moonshot score/analysis\", \"frontier tech stock\", \"disruptive company\", or investment analysis of AI, space, energy, biotech, quantum, cybersecurity, defense tech, digital finance companies. Covers megatrend alignment, technology readiness, de-risking progression, asymmetric upside, growth trajectory, team execution, and financial runway. Includes discovery scan, deep dive, and monitoring modes."
---

# Moonshot Analyzer — Framework v3

A systematic, 7-dimension scoring framework for evaluating high-risk/high-reward "moonshot" investment opportunities in companies riding structural megatrends with breakthrough technology and asymmetric risk/reward profiles.

> **Disclaimer**: This framework is an analytical tool, NOT investment advice. Moonshot investments carry extreme risk including potential total loss. Always do your own research and consult a qualified financial advisor.

---

## Operating Modes

This skill operates in three distinct modes:

| Mode | Purpose | Output |
|------|---------|--------|
| **Mode 1: Discovery Scan** | Broad market sweep across 15 megatrend categories to identify candidates | Ranked list of 15-25 candidates with Quick Scores (/35) |
| **Mode 2: Deep Dive** | Full 7-dimension analysis of a single company | Complete Moonshot Scorecard (100-point scale) with scenario analysis |
| **Mode 3: Monitoring** | Track existing positions and update scores based on new developments | Updated scorecard with delta tracking and catalyst status |

When the user's request is ambiguous, ask which mode they want. Default to **Deep Dive** if they name a specific ticker.

---

## Prerequisites

This skill requires **web search** capabilities to gather current financial data, SEC filings, analyst ratings, and news. It works best with:
- `WebSearch` — for current stock data, news, analyst coverage
- `WebFetch` — for reading earnings reports, SEC filings, press releases

If web tools are unavailable, the skill can still operate using data the user provides manually, but the analysis will be limited to the information given.

---

## Mode 1: Discovery Scan

### Purpose
Sweep across 15 megatrend categories to surface under-the-radar companies with moonshot potential. Target profile: market cap <$5B, low analyst coverage, structural megatrend exposure, early growth curve position.

### 15 Megatrend Categories

1. AI & Automation
2. Robotics & Autonomous Systems
3. Autonomous Mobility & eVTOL
4. Energy Transition
5. Next-Gen Connectivity (Photonics / 5G-6G)
6. Space Economy
7. Longevity & BioTech
8. Multiomics & AI-Native Biology
9. Cybersecurity
10. Digital Finance & Blockchain
11. Defense & Geopolitical Restructuring
12. 3D Printing / Additive Manufacturing
13. Water, Food & Climate
14. Demographic Shift & Silver Economy
15. Quantum Computing

### 4-Layer Search Methodology

For each megatrend, apply these four lenses:

1. **Supply Chain Depth** — Look beyond the obvious "headline" companies. Who supplies them? Who makes the picks and shovels? Which component maker is hidden 2-3 layers deep in the supply chain?
2. **Small Fish, Big Pond** — Find micro/small-caps ($50M-$2B) operating in massive TAMs ($100B+). The math of small revenue base + huge addressable market creates asymmetric potential.
3. **Contra-Signal** — Screen for stocks that are DOWN 40-70% from highs while their fundamentals are actually IMPROVING (revenue up, backlog growing, new contracts). The market is often wrong at extremes.
4. **Capital Deployment** — Track where smart money is flowing: insider buying clusters, government grants (CHIPS Act, DoE, DoD), and strategic corporate investments (Amazon backing BETA, IonQ acquiring SKYT).

### Quick Score Methodology (/35)

For each candidate, assign 1-5 points across 7 dimensions:

| # | Dimension | Character Question |
|---|-----------|-------------------|
| D1 | Megatrend & TAM | "How big is the wave?" |
| D2 | Technology & Breakthrough | "Is the innovation real?" |
| D3 | De-risking Progression | "Is risk declining?" |
| D4 | Asymmetric Risk/Reward | "Is the math in our favor?" |
| D5 | Growth Trajectory | "How fast, how scalable?" |
| D6 | Team & Execution | "Can these people deliver?" |
| D7 | Financial Runway & Burn | "Will the money last?" |

### Discovery Scan Output Format

```
# MOONSHOT DISCOVERY SCAN

**Date**: [Date]
**Analyst**: Moonshot Analyzer Framework v3
**Target Profile**: Market cap <$5B, low analyst coverage, structural megatrend, early growth curve

## TOP 25 CANDIDATES TABLE
[Ranked table with: #, Ticker, Company, Megatrend(s), Mcap, Quick Score /35]

## PER-MEGATREND BREAKDOWN
[For each of the 15 megatrends:]
### MEGATREND N: [Name]
#### [Company] ([Ticker]) — [Mcap]
**What they do**: [1-2 sentences]
**Why moonshot**: [Key thesis in 2-3 sentences]
[D1-D7 quick score table]
**Catalysts**: [Key upcoming catalysts]
**Risk**: [Primary risks]

## PRIORITY LIST — TOP 10 FOR DEEP DIVE
[Ranked table with deep dive rationale]

## THEMATIC SIGNALS
- Multi-Trend Intersection areas
- Contra-Signal opportunities
- Insider Buying signals

## GOOGLE SHEETS EXPORT
[Pipe-delimited export row for each candidate]
```

---

## Mode 2: Deep Dive

### Purpose
Full 7-dimension analysis of a single company producing a 100-point Moonshot Scorecard.

### Step 1: Data Gathering

Use web search to collect:
- Current stock price, market cap, shares outstanding, short interest
- Last 2-4 quarterly earnings (revenue, margins, cash flow, guidance)
- SEC filings (10-K, 10-Q) for detailed financials
- Analyst ratings and price targets
- Insider trading activity (last 6 months)
- Recent news, contracts, partnerships, regulatory updates
- Competitive landscape and industry dynamics

### Step 2: Dimension Scoring

Each dimension is scored 0-100 using weighted sub-metrics. Sub-metrics are scored 1-10, then multiplied by their weight to produce weighted scores.

#### Dimension 1: Megatrend & TAM (Weight: 20%)

| Sub-Metric | Weight | What to Evaluate |
|------------|--------|-----------------|
| TAM Size | 1.3x | Total addressable market in 2030+ dollars |
| Structural vs Cyclical | 1.2x | Is this a permanent shift or a cycle? |
| Trend Intersection | 1.5x | How many megatrends does the company sit at? |
| Impossible-to-Inevitable | 1.3x | Where is the narrative on the adoption curve? |

**Scoring Guide**:
- 9-10: TAM >$500B, structural + irreversible, 3+ megatrend intersection
- 7-8: TAM $100-500B, structural, 2 megatrend intersection
- 5-6: TAM $50-100B, mostly structural, single megatrend
- 3-4: TAM <$50B or partially cyclical
- 1-2: Small/uncertain TAM or largely cyclical

#### Dimension 2: Technology & Breakthrough (Weight: 20%)

| Sub-Metric | Weight | What to Evaluate |
|------------|--------|-----------------|
| Technology Readiness (TRL) | 1.3x | NASA TRL scale 1-9 |
| 10x Improvement | 1.5x | Does the tech offer 10x better/cheaper/faster? |
| Technical Moat | 1.2x | IP, trade secrets, regulatory barriers |
| R&D Intensity | 1.0x | R&D spend as % of revenue, patent pipeline |
| Parameter Completeness | 1.4x | Are key technical specs proven? |
| Breakthrough Dependency | 1.5x | Does it need a scientific breakthrough to work? |
| Ecosystem Lock-in | 1.3x | Switching costs, network effects, standards |

**Scoring Guide**:
- 9-10: TRL 8-9, proven 10x improvement, strong IP moat, no breakthrough needed
- 7-8: TRL 6-7, clear 3-5x improvement, solid moat
- 5-6: TRL 4-5, incremental improvement, moderate moat
- 3-4: TRL 2-3, theoretical improvement, weak moat
- 1-2: TRL 1, unproven concept, no moat

#### Dimension 3: De-risking Progression (Weight: 15%)

| Sub-Metric | Weight | What to Evaluate |
|------------|--------|-----------------|
| Milestone Completion | 1.5x | Key milestones hit in last 12 months |
| Regulatory Progress | 1.3x | FDA/FAA/FCC/NRC approvals, certifications |
| Revenue Inflection | 1.3x | Revenue growth acceleration, backlog growth |
| Technology Validation | 1.0x | Third-party validation, peer review, demos |
| Risk Map Narrowing | 1.2x | How many major risks have been eliminated? |

**Scoring Guide**:
- 9-10: Multiple major milestones hit, regulatory approved, revenue inflecting up
- 7-8: Several milestones hit, regulatory on track, revenue growing
- 5-6: Some milestones hit, regulatory filed, early revenue
- 3-4: Few milestones, regulatory uncertain, pre-revenue
- 1-2: No milestones, no regulatory path, no revenue

#### Dimension 4: Asymmetric Risk/Reward (Weight: 15%)

| Sub-Metric | Weight | What to Evaluate |
|------------|--------|-----------------|
| Upside Scenario | 1.5x | 5-year bull case multiple (vs current price) |
| Downside Scenario | 1.3x | Floor price / asset value protection |
| Asymmetry Ratio | 1.5x | Bull/Bear ratio (target: >5x) |
| Optionality | 1.2x | Hidden options, pivot potential, M&A target |
| Narrative Cycle Position | 1.3x | Hype cycle position (trough = best entry) |

**Scoring Guide**:
- 9-10: >10x upside, limited downside, trough of disillusionment entry
- 7-8: 5-10x upside, moderate downside protection, early narrative
- 5-6: 3-5x upside, some downside risk, mid-narrative
- 3-4: <3x upside or significant downside risk
- 1-2: Limited upside or high downside, peak narrative

**Required Output — Scenario Table**:

| Scenario | Probability | 5Y Price Target | Multiple |
|----------|-------------|-----------------|----------|
| Bull | [%] | [$] | [x] |
| Base | [%] | [$] | [x] |
| Bear | [%] | [$] | [x] |

#### Dimension 5: Growth Trajectory (Weight: 12%)

| Sub-Metric | Weight | What to Evaluate |
|------------|--------|-----------------|
| Revenue Growth Rate | 1.3x | YoY revenue growth |
| Market Penetration | 1.2x | Current % of TAM captured |
| Customer Acquisition | 1.0x | New customer wins, pipeline |
| Product Line Breadth | 1.2x | Revenue stream diversification |
| Hyperscalability | 1.5x | Can revenue grow without proportional cost? |
| Geographic Expansion | 0.8x | International market entry |

#### Dimension 6: Team & Execution (Weight: 8%)

| Sub-Metric | Weight | What to Evaluate |
|------------|--------|-----------------|
| Founder/CEO Profile | 1.5x | Domain expertise, track record |
| Skin in the Game | 1.3x | Insider ownership %, recent buying |
| Execution Track Record | 1.5x | Promises made vs delivered |
| Team Depth | 1.0x | Key hires, board quality |
| Strategic Hires | 0.8x | Recent hires signaling direction |
| Product Focus Score | 1.4x | Focused vs scattered strategy |

#### Dimension 7: Financial Runway & Burn (Weight: 10%)

| Sub-Metric | Weight | What to Evaluate |
|------------|--------|-----------------|
| Cash Runway | 1.5x | Months of cash at current burn rate |
| Dilution Risk | 1.3x | Secondary offering risk, warrant overhang |
| Capital Access | 1.0x | Debt facilities, government grants |
| Path to Profitability | 1.2x | Timeline to positive cash flow |
| Gross Margin Trend | 1.0x | Improving or declining margins |

### Step 3: Knockout Filters

After scoring, apply these binary filters:

| Filter | Condition | Action |
|--------|-----------|--------|
| Breakthrough Overload | Company needs >=3 unproven breakthroughs | Penalty: -15 points |
| Cash Crunch | <6 months runway, no funding path | Penalty: -20 points |
| Insider Exodus | Major insider selling >20% in 6 months | Penalty: -10 points |
| Product Scatter | >5 unrelated product lines, no focus | Penalty: -10 points |
| Hype Peak | At peak of hype cycle with max retail attention | Penalty: -10 points |
| Trough Entry Bonus | At trough of disillusionment with improving fundamentals | Bonus: +5 points |
| Multi-Trend Bonus | Sits at intersection of 3+ megatrends | Bonus: +3 points |
| De-risk Acceleration | Major de-risking event in last 3 months | Bonus: +5 points |

### Step 4: Final Score Calculation

```
Raw Score = (D1 × 0.20) + (D2 × 0.20) + (D3 × 0.15) + (D4 × 0.15) + (D5 × 0.12) + (D6 × 0.08) + (D7 × 0.10)
Final Adjusted Score = Raw Score + Knockout Adjustments (capped at +/- 20)
```

### Verdict Classification

| Score Range | Verdict | Risk Profile | Position Size |
|-------------|---------|--------------|---------------|
| 80-100 | STRONG BUY CONVICTION | Aggressive Moonshot | 2-3% of portfolio |
| 70-79 | HIGH CONVICTION WATCH | Moderate Moonshot | 1-2% of portfolio |
| 60-69 | SPECULATIVE WATCH | High Risk Moonshot | 0.5-1% of portfolio |
| 50-59 | MONITOR ONLY | Very High Risk | 0% until catalysts |
| <50 | PASS | Unacceptable Risk | Avoid |

**Total moonshot allocation should stay under 10-15% of total portfolio.**

### Deep Dive Output Format

```
# [TICKER] — [Company Name] Moonshot Analysis

**Date**: [Date]
**Analyst**: Moonshot Analyzer Framework v3
**Current Price**: $[X] | **Market Cap**: $[X] | **Exchange**: [X]

---

## Moonshot Scorecard
[ASCII scorecard with all 7 dimensions, bar charts, weights, and final score]

## Executive Summary
[2-3 paragraph thesis]
**Megatrend(s)**: [Primary + Secondary]
**One-liner**: "[Elevator pitch quote]"

## Dimension Breakdown
[For each of 7 dimensions:]
### N. [Dimension Name] — [Score]/100
[Sub-metric table with Score, Weight, Weighted Score]
**Analysis**: [2-3 paragraph detailed analysis]

## Bull vs Bear
[Two-column table]

## Knockout Filter Results
[Table with each filter status and impact]

## Warning Flags
[Bullet list of concerns]

## Key Catalysts (Next 6-18 Months)
[Table: Catalyst, Expected Timeline, Potential Impact]

## Final Verdict
[ASCII verdict box with score, risk profile, position size, key conditions]

## Google Sheets Export Row
[Single pipe-delimited row for spreadsheet tracking]
```

---

## Mode 3: Monitoring

### Purpose
Update an existing Moonshot Scorecard based on new developments.

### Process
1. Load the previous scorecard (user provides or references)
2. Search for developments since the last analysis date
3. Re-score any dimensions affected by new information
4. Track score deltas (was 72, now 68 = -4)
5. Update catalyst status (hit/missed/delayed)
6. Flag any new knockout filter triggers
7. Recommend action: HOLD / ADD / TRIM / EXIT

### Monitoring Output Additions
- **Score Delta**: Previous → Current with arrow
- **Catalyst Tracker**: Status of each previously identified catalyst
- **New Developments**: Bullet list of material changes since last report
- **Action Recommendation**: Based on score change direction and magnitude

---

## Configuration

The framework supports user-level customization. At the start of a conversation, the user may specify preferences that override defaults. If not specified, use the defaults below.

### Language

| Setting | Default | Options |
|---------|---------|---------|
| Output language | Match user's language | Turkish, English, or any language the user writes in |

**Rule**: If the user writes in Turkish, respond in Turkish. If in English, respond in English. If the user explicitly requests a language ("Analyze in English"), use that language regardless of conversation language.

### Risk Profile

| Setting | Default | Conservative | Aggressive |
|---------|---------|-------------|------------|
| Max per-position | 2% | 0.5% | 3% |
| Max total moonshot allocation | 10-15% | 5% | 20% |
| Minimum score for position | 60 | 70 | 50 |

If the user specifies their risk tolerance, adjust position sizing recommendations accordingly. Always state the risk profile being used in the Final Verdict.

### Output Format

| Setting | Default | Options |
|---------|---------|---------|
| Report detail level | Full (all sections) | `full` — complete report with all sections |
| | | `compact` — scorecard + verdict + key catalysts only |
| | | `scorecard-only` — just the ASCII scorecard box |
| Spreadsheet export | Included (pipe-delimited row) | Google Sheets row, `.xlsx` dashboard, or skip |
| Scenario table | Always included | Can be skipped if user says "skip scenarios" |

### Sector Focus

| Setting | Default | Options |
|---------|---------|---------|
| Megatrend scope | All 15 categories | User can include/exclude specific megatrends |
| Market cap range | <$5B | User can adjust (e.g., "<$2B" or "<$10B") |
| Exchange filter | All US exchanges | Can filter to NASDAQ only, NYSE only, etc. |
| Exclude list | None | User can exclude specific tickers or sectors |

### Data Sources

| Setting | Default | When unavailable |
|---------|---------|------------------|
| Stock price | Live via WebSearch | User provides manually |
| Financials | Latest 10-Q/10-K via WebSearch | User provides or use last known |
| Analyst ratings | Live via WebSearch | Skip or user provides |
| Insider activity | Live via WebSearch | Skip or user provides |
| News/catalysts | Live via WebSearch | User provides or use last known |

**Critical rule**: Always clearly state the data date in the report header. If any data is stale (>30 days old), flag it with a warning.

### Monitoring Configuration

| Setting | Default | Options |
|---------|---------|---------|
| Update trigger | On user request | Can be scheduled (monthly, quarterly) |
| Alert threshold | Any score change | User can set minimum delta (e.g., ">5 points") |
| Knockout alert | Always alert | Can be set to alert only on new triggers |

---

## Important Notes

### Data Freshness
- Always note the date of analysis prominently in the report header
- Financial data should be from the most recent available quarter
- Stock prices should be current-day (from web search)
- If any data point is older than 30 days, flag it: `[DATA: as of YYYY-MM-DD]`
- If web search is unavailable, clearly state: "Analysis based on user-provided data only"

### Limitations
- This is a scoring framework, not investment advice
- Moonshot stocks are inherently high-risk — most will fail
- Past scores do not predict future performance
- The framework has biases toward technology-heavy sectors
- Always include the disclaimer in every output
- Scores are point-in-time snapshots — a company's score can change dramatically with a single event

### Complementary Frameworks
- **Warren Buffett Analyst**: For proven profitable companies with established moats — use for the stable core of a portfolio
- **Moonshot Analyzer**: For pre-profit or early-growth companies riding structural megatrends — use for the high-risk satellite allocation
- Use both together for a balanced barbell portfolio approach (80-90% value core + 10-15% moonshot satellite)
