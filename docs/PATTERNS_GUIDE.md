# Trading Patterns Visualization Guide

This guide explains all the detected patterns, their symbols, colors, and trading implications.

---

## 1. HEAD & SHOULDER PATTERNS
**File**: `outputs/01_head_shoulder.png`

| Pattern | Symbol | Color | Position | Signal |
|---------|--------|-------|----------|--------|
| Head & Shoulder | ▼ (v) | Red | At High | Bearish Reversal ⬇️ |
| Inverse H&S | ▲ (^) | Green | At Low | Bullish Reversal ⬆️ |

**Trading Implication**: Major reversal patterns. H&S suggests downtrend, Inverse H&S suggests uptrend.

---

## 2. DOUBLE TOP & BOTTOM PATTERNS
**File**: `outputs/02_double_top_bottom.png`

| Pattern | Symbol | Color | Position | Signal |
|---------|--------|-------|----------|--------|
| Double Top | ✖ (X) | Red | At High | Bearish Reversal ⬇️ |
| Double Bottom | ✖ (X) | Green | At Low | Bullish Reversal ⬆️ |

**Trading Implication**: Strong reversal patterns formed when price tests same level twice.

---

## 3. MULTIPLE TOPS & BOTTOMS
**File**: `outputs/03_multiple_tops_bottoms.png`

| Pattern | Symbol | Color | Position | Signal |
|---------|--------|-------|----------|--------|
| Multiple Top | ◆ (D) | Red | At High | Resistance Level 🛑 |
| Multiple Bottom | ◆ (D) | Green | At Low | Support Level 🛡️ |

**Trading Implication**: Price testing resistance/support multiple times.

---

## 4. TRIANGLE PATTERNS
**File**: `outputs/04_triangle_patterns.png`

| Pattern | Symbol | Color | Position | Signal |
|---------|--------|-------|----------|--------|
| Ascending Triangle | ▲ (^) | Blue | At Low | Bullish Continuation ⬆️ |
| Descending Triangle | ▼ (v) | Orange | At High | Bearish Continuation ⬇️ |

**Trading Implication**: Continuation patterns. Ascending = bullish, Descending = bearish.

---

## 5. WEDGE PATTERNS
**File**: `outputs/05_wedge_patterns.png`

| Pattern | Symbol | Color | Position | Signal |
|---------|--------|-------|----------|--------|
| Wedge Up | ⬟ (P) | Green | At Low | Potential Reversal Down ⚠️ |
| Wedge Down | ⬟ (P) | Red | At High | Potential Reversal Up ⚠️ |

**Trading Implication**: Wedges often lead to reversals. Rising wedge = bearish, Falling wedge = bullish.

---

## 6. CHANNEL PATTERNS
**File**: `outputs/06_channel_patterns.png`

| Pattern | Symbol | Color | Position | Signal |
|---------|--------|-------|----------|--------|
| Channel Up | ■ (s) | Cyan | At Low | Bullish Trend 📈 |
| Channel Down | ■ (s) | Magenta | At High | Bearish Trend 📉 |

**Trading Implication**: Price moving in parallel channels. Trade within the channel.

---

## 7. SUPPORT & RESISTANCE LEVELS
**File**: `outputs/07_support_resistance.png`

| Element | Style | Color | Signal |
|---------|-------|-------|--------|
| Support | Dashed Line (--) | Green | Price Floor 🛡️ |
| Resistance | Dashed Line (--) | Red | Price Ceiling 🛑 |

**Trading Implication**: Key price levels. Buy near support, sell near resistance.

---

## 8. PIVOT POINTS (Market Structure)
**File**: `outputs/08_pivot_points.png`

| Pattern | Symbol | Color | Position | Signal |
|---------|--------|-------|----------|--------|
| Higher High (HH) | ▲ (^) | Dark Green | At High | Uptrend Strong 💪 |
| Lower Low (LL) | ▼ (v) | Dark Red | At Low | Downtrend Strong 💪 |
| Lower High (LH) | ▼ (v) | Orange | At High | Uptrend Weakening ⚠️ |
| Higher Low (HL) | ▲ (^) | Light Blue | At Low | Downtrend Weakening ⚠️ |

**Trading Implication**: 
- **Uptrend**: HH + HL (higher highs and higher lows)
- **Downtrend**: LH + LL (lower highs and lower lows)
- **Trend Change**: When pattern breaks

---

## 9. ALL PATTERNS COMBINED
**File**: `outputs/09_all_patterns_combined.png`

Shows major patterns together for comprehensive market view.

---

## Pattern Filtering

All patterns use 3-stage filtering:
1. **Clustering**: Groups nearby patterns (within 10 bars)
2. **Distance**: Ensures 15+ bars between patterns
3. **Strength**: Selects top patterns by price volatility

This ensures only the **best and most significant patterns** are displayed.

---

## Trading Strategy Tips

### Bullish Signals (Buy/Long):
- ✅ Inverse Head & Shoulder at bottom
- ✅ Double Bottom
- ✅ Higher Lows (HL) forming
- ✅ Ascending Triangle breakout
- ✅ Price bouncing off Support

### Bearish Signals (Sell/Short):
- ❌ Head & Shoulder at top
- ❌ Double Top
- ❌ Lower Highs (LH) forming
- ❌ Descending Triangle breakdown
- ❌ Price rejected at Resistance

### Confirmation:
Always wait for **volume confirmation** and **price breakout/breakdown** before trading!

---

**Note**: These are detected patterns based on technical analysis. Always combine with other indicators and risk management for actual trading decisions.

