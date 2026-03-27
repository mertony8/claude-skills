# Moonshot Analyzer — Scoring Methodology Reference

## Dimension Weight Rationale

The 7 dimensions are weighted to reflect what matters most for moonshot investing:

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| D1: Megatrend & TAM | 20% | The wave matters more than the surfer. A mediocre company on a massive megatrend can still return 5-10x. |
| D2: Technology & Breakthrough | 20% | Real innovation is what separates moonshots from penny stocks. Must be provable and defensible. |
| D3: De-risking Progression | 15% | Momentum in risk reduction is the strongest signal that a thesis is playing out. |
| D4: Asymmetric R/R | 15% | The entire point of moonshot investing — small position, huge potential upside, survivable downside. |
| D5: Growth Trajectory | 12% | Revenue growth and scalability validate the market opportunity. |
| D6: Team & Execution | 8% | Important but overweighted by most frameworks. A great team on the wrong wave still loses. |
| D7: Financial Runway | 10% | Cash is oxygen. Companies that run out of it die, regardless of how good the technology is. |

## Sub-Metric Weights

Sub-metric weights within each dimension are calibrated on a 0.8x-1.5x scale:

- **1.5x** — Critical differentiator (e.g., Breakthrough Dependency in D2, Cash Runway in D7)
- **1.3x** — Important factor
- **1.2x** — Meaningful factor
- **1.0x** — Standard factor
- **0.8x** — Context factor (useful but not decisive)

## Knockout Filter Logic

### Penalties (negative adjustments)

**Breakthrough Overload (-15)**: If a company needs 3 or more unproven scientific breakthroughs to work, the probability of all three succeeding is too low. Even at 50% per breakthrough, P(all 3) = 12.5%.

**Cash Crunch (-20)**: Less than 6 months of cash with no clear funding path is an existential risk. The stock will likely do a dilutive offering or go bankrupt. Largest penalty because death is permanent.

**Insider Exodus (-10)**: When insiders sell >20% of holdings in 6 months, they're telling you something. Small sales for tax/diversification are normal; large coordinated selling is a red flag.

**Product Scatter (-10)**: Companies with >5 unrelated product lines are likely unfocused. Moonshot success requires intense focus on a single breakthrough.

**Hype Peak (-10)**: At the peak of the hype cycle, expectations are priced in and any disappointment causes massive drawdowns. Best entry is at the trough.

### Bonuses (positive adjustments)

**Trough Entry (+5)**: Buying when sentiment is at maximum negative but fundamentals are improving is the highest-probability moonshot entry.

**Multi-Trend (+3)**: Companies at the intersection of 3+ megatrends have multiple ways to win. If one trend slows, others can carry them.

**De-risk Acceleration (+5)**: A major de-risking event in the last 3 months (FDA approval, major contract, acquisition offer) changes the risk profile faster than quarterly scoring captures.

## Score Normalization

Raw sub-metric scores are on a 1-10 scale. To convert to the 0-100 dimension score:

1. Calculate weighted sum: `sum(score_i * weight_i)`
2. Calculate max possible: `sum(10 * weight_i)`
3. Normalize: `(weighted_sum / max_possible) * 100`

## Scenario Analysis Framework

For the Asymmetric R/R dimension, always build three scenarios:

### Bull Case
- Assume all key catalysts hit
- Best reasonable outcome in 5 years
- Assign probability (typically 15-30%)

### Base Case
- Assume partial catalyst success
- Most likely outcome
- Assign probability (typically 40-60%)

### Bear Case
- Assume major catalysts miss
- Worst reasonable outcome (not bankruptcy unless realistic)
- Assign probability (typically 15-30%)

### Risk-Adjusted Expected Value
```
RAEV = (P_bull * Target_bull) + (P_base * Target_base) + (P_bear * Target_bear)
```

Compare RAEV to current price. If RAEV/Current > 2x, asymmetry is favorable.

## Quick Score vs Deep Dive Mapping

The Quick Score (/35) maps approximately to the Deep Dive (/100):

| Quick Score | Approximate Deep Dive Equivalent |
|-------------|--------------------------------|
| 30-35 | 80-100 (Strong Buy Conviction) |
| 25-29 | 65-79 (High Conviction Watch) |
| 20-24 | 50-64 (Speculative Watch) |
| 15-19 | 35-49 (Monitor / Pass) |
| <15 | <35 (Pass) |

This mapping is approximate. The Deep Dive adds nuance through weighted sub-metrics and knockout filters that the Quick Score cannot capture.
