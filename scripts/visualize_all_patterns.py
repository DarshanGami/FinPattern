"""
Comprehensive Trading Pattern Visualization Script
Detects and visualizes all trading patterns with best filtering
Generates 9 separate chart images
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import mplfinance as mpf
import yfinance as yf

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tradingpatterns import (
    detect_head_shoulder,
    detect_multiple_tops_bottoms,
    detect_triangle_pattern,
    detect_wedge,
    detect_channel,
    detect_double_top_bottom,
    calculate_support_resistance,
    find_pivots,
    filter_best_patterns
)

def main():
    # Setup output directory
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs')
    os.makedirs(output_dir, exist_ok=True)
    
    # Download and prepare data
    print("Downloading BTC-USD data...")
    df = yf.download("BTC-USD", period="6mo", interval="1d", auto_adjust=False)
    # Flatten MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    ohlc = df[["Open", "High", "Low", "Close"]].copy()
    
    print(f"Data loaded: {len(ohlc)} candles\n")
    
    # 1. HEAD & SHOULDER PATTERNS
    print("=" * 60)
    print("1. HEAD & SHOULDER PATTERNS")
    print("=" * 60)
    work_hs = detect_head_shoulder(ohlc.reset_index(drop=True).copy(), window=5)
    hs_pos = np.where(work_hs["head_shoulder_pattern"] == "Head and Shoulder")[0]
    inv_hs_pos = np.where(work_hs["head_shoulder_pattern"] == "Inverse Head and Shoulder")[0]
    
    hs_pos = filter_best_patterns(hs_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    inv_hs_pos = filter_best_patterns(inv_hs_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    
    print(f"Found {len(hs_pos)} Head & Shoulder patterns")
    print(f"Found {len(inv_hs_pos)} Inverse Head & Shoulder patterns")
    
    hs_markers = pd.Series(np.nan, index=ohlc.index)
    hs_markers.iloc[hs_pos] = ohlc["High"].iloc[hs_pos]
    inv_hs_markers = pd.Series(np.nan, index=ohlc.index)
    inv_hs_markers.iloc[inv_hs_pos] = ohlc["Low"].iloc[inv_hs_pos]
    
    mpf.plot(
        ohlc,
        type="candle",
        style="yahoo",
        addplot=[
            mpf.make_addplot(hs_markers, type="scatter", marker="v", color="red", markersize=80),
            mpf.make_addplot(inv_hs_markers, type="scatter", marker="^", color="green", markersize=80),
        ],
        volume=False,
        title="BTC-USD: Head & Shoulder Patterns",
        savefig=os.path.join(output_dir, "01_head_shoulder.png")
    )
    print("✓ Saved: outputs/01_head_shoulder.png\n")
    
    # 2. DOUBLE TOP & BOTTOM PATTERNS
    print("=" * 60)
    print("2. DOUBLE TOP & BOTTOM PATTERNS")
    print("=" * 60)
    work_double = detect_double_top_bottom(ohlc.reset_index(drop=True).copy(), window=5, threshold=0.05)
    double_top_pos = np.where(work_double["double_pattern"] == "Double Top")[0]
    double_bottom_pos = np.where(work_double["double_pattern"] == "Double Bottom")[0]
    
    double_top_pos = filter_best_patterns(double_top_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    double_bottom_pos = filter_best_patterns(double_bottom_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    
    print(f"Found {len(double_top_pos)} Double Top patterns")
    print(f"Found {len(double_bottom_pos)} Double Bottom patterns")
    
    dt_markers = pd.Series(np.nan, index=ohlc.index)
    dt_markers.iloc[double_top_pos] = ohlc["High"].iloc[double_top_pos]
    db_markers = pd.Series(np.nan, index=ohlc.index)
    db_markers.iloc[double_bottom_pos] = ohlc["Low"].iloc[double_bottom_pos]
    
    mpf.plot(
        ohlc,
        type="candle",
        style="yahoo",
        addplot=[
            mpf.make_addplot(dt_markers, type="scatter", marker="X", color="red", markersize=100),
            mpf.make_addplot(db_markers, type="scatter", marker="X", color="green", markersize=100),
        ],
        volume=False,
        title="BTC-USD: Double Top & Bottom Patterns",
        savefig=os.path.join(output_dir, "02_double_top_bottom.png")
    )
    print("✓ Saved: outputs/02_double_top_bottom.png\n")
    
    # 3. MULTIPLE TOPS & BOTTOMS
    print("=" * 60)
    print("3. MULTIPLE TOPS & BOTTOMS")
    print("=" * 60)
    work_multiple = detect_multiple_tops_bottoms(ohlc.reset_index(drop=True).copy(), window=5)
    multi_top_pos = np.where(work_multiple["multiple_top_bottom_pattern"] == "Multiple Top")[0]
    multi_bottom_pos = np.where(work_multiple["multiple_top_bottom_pattern"] == "Multiple Bottom")[0]
    
    multi_top_pos = filter_best_patterns(multi_top_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    multi_bottom_pos = filter_best_patterns(multi_bottom_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    
    print(f"Found {len(multi_top_pos)} Multiple Top patterns")
    print(f"Found {len(multi_bottom_pos)} Multiple Bottom patterns")
    
    if len(multi_top_pos) > 0 or len(multi_bottom_pos) > 0:
        addplots = []
        if len(multi_top_pos) > 0:
            mt_markers = pd.Series(np.nan, index=ohlc.index)
            mt_markers.iloc[multi_top_pos] = ohlc["High"].iloc[multi_top_pos]
            addplots.append(mpf.make_addplot(mt_markers, type="scatter", marker="D", color="red", markersize=60))
        if len(multi_bottom_pos) > 0:
            mb_markers = pd.Series(np.nan, index=ohlc.index)
            mb_markers.iloc[multi_bottom_pos] = ohlc["Low"].iloc[multi_bottom_pos]
            addplots.append(mpf.make_addplot(mb_markers, type="scatter", marker="D", color="green", markersize=60))
        
        mpf.plot(
            ohlc,
            type="candle",
            style="yahoo",
            addplot=addplots,
            volume=False,
            title="BTC-USD: Multiple Tops & Bottoms",
            savefig=os.path.join(output_dir, "03_multiple_tops_bottoms.png")
        )
        print("✓ Saved: outputs/03_multiple_tops_bottoms.png\n")
    else:
        print("⚠ Skipped: No patterns found\n")
    
    # 4. TRIANGLE PATTERNS
    print("=" * 60)
    print("4. TRIANGLE PATTERNS")
    print("=" * 60)
    work_triangle = detect_triangle_pattern(ohlc.reset_index(drop=True).copy(), window=5)
    asc_triangle_pos = np.where(work_triangle["triangle_pattern"] == "Ascending Triangle")[0]
    desc_triangle_pos = np.where(work_triangle["triangle_pattern"] == "Descending Triangle")[0]
    
    asc_triangle_pos = filter_best_patterns(asc_triangle_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    desc_triangle_pos = filter_best_patterns(desc_triangle_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    
    print(f"Found {len(asc_triangle_pos)} Ascending Triangle patterns")
    print(f"Found {len(desc_triangle_pos)} Descending Triangle patterns")
    
    if len(asc_triangle_pos) > 0 or len(desc_triangle_pos) > 0:
        addplots = []
        if len(asc_triangle_pos) > 0:
            at_markers = pd.Series(np.nan, index=ohlc.index)
            at_markers.iloc[asc_triangle_pos] = ohlc["Low"].iloc[asc_triangle_pos]
            addplots.append(mpf.make_addplot(at_markers, type="scatter", marker="^", color="blue", markersize=80))
        if len(desc_triangle_pos) > 0:
            dt_tri_markers = pd.Series(np.nan, index=ohlc.index)
            dt_tri_markers.iloc[desc_triangle_pos] = ohlc["High"].iloc[desc_triangle_pos]
            addplots.append(mpf.make_addplot(dt_tri_markers, type="scatter", marker="v", color="orange", markersize=80))
        
        mpf.plot(
            ohlc,
            type="candle",
            style="yahoo",
            addplot=addplots,
            volume=False,
            title="BTC-USD: Triangle Patterns",
            savefig=os.path.join(output_dir, "04_triangle_patterns.png")
        )
        print("✓ Saved: outputs/04_triangle_patterns.png\n")
    else:
        print("⚠ Skipped: No patterns found\n")
    
    # 5. WEDGE PATTERNS
    print("=" * 60)
    print("5. WEDGE PATTERNS")
    print("=" * 60)
    work_wedge = detect_wedge(ohlc.reset_index(drop=True).copy(), window=5)
    wedge_up_pos = np.where(work_wedge["wedge_pattern"] == "Wedge Up")[0]
    wedge_down_pos = np.where(work_wedge["wedge_pattern"] == "Wedge Down")[0]
    
    wedge_up_pos = filter_best_patterns(wedge_up_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    wedge_down_pos = filter_best_patterns(wedge_down_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    
    print(f"Found {len(wedge_up_pos)} Wedge Up patterns")
    print(f"Found {len(wedge_down_pos)} Wedge Down patterns")
    
    if len(wedge_up_pos) > 0 or len(wedge_down_pos) > 0:
        addplots = []
        if len(wedge_up_pos) > 0:
            wu_markers = pd.Series(np.nan, index=ohlc.index)
            wu_markers.iloc[wedge_up_pos] = ohlc["Low"].iloc[wedge_up_pos]
            addplots.append(mpf.make_addplot(wu_markers, type="scatter", marker="P", color="green", markersize=80))
        if len(wedge_down_pos) > 0:
            wd_markers = pd.Series(np.nan, index=ohlc.index)
            wd_markers.iloc[wedge_down_pos] = ohlc["High"].iloc[wedge_down_pos]
            addplots.append(mpf.make_addplot(wd_markers, type="scatter", marker="P", color="red", markersize=80))
        
        mpf.plot(
            ohlc,
            type="candle",
            style="yahoo",
            addplot=addplots,
            volume=False,
            title="BTC-USD: Wedge Patterns",
            savefig=os.path.join(output_dir, "05_wedge_patterns.png")
        )
        print("✓ Saved: outputs/05_wedge_patterns.png\n")
    else:
        print("⚠ Skipped: No patterns found\n")
    
    # 6. CHANNEL PATTERNS
    print("=" * 60)
    print("6. CHANNEL PATTERNS")
    print("=" * 60)
    work_channel = detect_channel(ohlc.reset_index(drop=True).copy(), window=5)
    channel_up_pos = np.where(work_channel["channel_pattern"] == "Channel Up")[0]
    channel_down_pos = np.where(work_channel["channel_pattern"] == "Channel Down")[0]
    
    channel_up_pos = filter_best_patterns(channel_up_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    channel_down_pos = filter_best_patterns(channel_down_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    
    print(f"Found {len(channel_up_pos)} Channel Up patterns")
    print(f"Found {len(channel_down_pos)} Channel Down patterns")
    
    if len(channel_up_pos) > 0 or len(channel_down_pos) > 0:
        addplots = []
        if len(channel_up_pos) > 0:
            cu_markers = pd.Series(np.nan, index=ohlc.index)
            cu_markers.iloc[channel_up_pos] = ohlc["Low"].iloc[channel_up_pos]
            addplots.append(mpf.make_addplot(cu_markers, type="scatter", marker="s", color="cyan", markersize=60))
        if len(channel_down_pos) > 0:
            cd_markers = pd.Series(np.nan, index=ohlc.index)
            cd_markers.iloc[channel_down_pos] = ohlc["High"].iloc[channel_down_pos]
            addplots.append(mpf.make_addplot(cd_markers, type="scatter", marker="s", color="magenta", markersize=60))
        
        mpf.plot(
            ohlc,
            type="candle",
            style="yahoo",
            addplot=addplots,
            volume=False,
            title="BTC-USD: Channel Patterns",
            savefig=os.path.join(output_dir, "06_channel_patterns.png")
        )
        print("✓ Saved: outputs/06_channel_patterns.png\n")
    else:
        print("⚠ Skipped: No patterns found\n")
    
    # 7. SUPPORT & RESISTANCE LEVELS
    print("=" * 60)
    print("7. SUPPORT & RESISTANCE LEVELS")
    print("=" * 60)
    work_sr = calculate_support_resistance(ohlc.reset_index(drop=True).copy(), window=20)
    
    support_line = pd.Series(work_sr["support"].values, index=ohlc.index)
    resistance_line = pd.Series(work_sr["resistance"].values, index=ohlc.index)
    
    mpf.plot(
        ohlc,
        type="candle",
        style="yahoo",
        addplot=[
            mpf.make_addplot(support_line, color="green", width=1.5, linestyle="--"),
            mpf.make_addplot(resistance_line, color="red", width=1.5, linestyle="--"),
        ],
        volume=False,
        title="BTC-USD: Support & Resistance Levels",
        savefig=os.path.join(output_dir, "07_support_resistance.png")
    )
    print("✓ Saved: outputs/07_support_resistance.png\n")
    
    # 8. PIVOT POINTS
    print("=" * 60)
    print("8. PIVOT POINTS (Market Structure)")
    print("=" * 60)
    work_pivots = ohlc.reset_index(drop=True).copy()
    work_pivots.columns = work_pivots.columns.str.lower()
    work_pivots = find_pivots(work_pivots)
    
    hh_pos = np.where(work_pivots["signal"] == "HH")[0]
    ll_pos = np.where(work_pivots["signal"] == "LL")[0]
    lh_pos = np.where(work_pivots["signal"] == "LH")[0]
    hl_pos = np.where(work_pivots["signal"] == "HL")[0]
    
    hh_pos = filter_best_patterns(hh_pos, ohlc, cluster_distance=8, min_distance=10, max_patterns=15)
    ll_pos = filter_best_patterns(ll_pos, ohlc, cluster_distance=8, min_distance=10, max_patterns=15)
    lh_pos = filter_best_patterns(lh_pos, ohlc, cluster_distance=8, min_distance=10, max_patterns=15)
    hl_pos = filter_best_patterns(hl_pos, ohlc, cluster_distance=8, min_distance=10, max_patterns=15)
    
    print(f"Found {len(hh_pos)} Higher Highs (HH)")
    print(f"Found {len(ll_pos)} Lower Lows (LL)")
    print(f"Found {len(lh_pos)} Lower Highs (LH)")
    print(f"Found {len(hl_pos)} Higher Lows (HL)")
    
    hh_markers = pd.Series(np.nan, index=ohlc.index)
    hh_markers.iloc[hh_pos] = ohlc["High"].iloc[hh_pos]
    ll_markers = pd.Series(np.nan, index=ohlc.index)
    ll_markers.iloc[ll_pos] = ohlc["Low"].iloc[ll_pos]
    lh_markers = pd.Series(np.nan, index=ohlc.index)
    lh_markers.iloc[lh_pos] = ohlc["High"].iloc[lh_pos]
    hl_markers = pd.Series(np.nan, index=ohlc.index)
    hl_markers.iloc[hl_pos] = ohlc["Low"].iloc[hl_pos]
    
    mpf.plot(
        ohlc,
        type="candle",
        style="yahoo",
        addplot=[
            mpf.make_addplot(hh_markers, type="scatter", marker="^", color="darkgreen", markersize=70),
            mpf.make_addplot(ll_markers, type="scatter", marker="v", color="darkred", markersize=70),
            mpf.make_addplot(lh_markers, type="scatter", marker="v", color="orange", markersize=70),
            mpf.make_addplot(hl_markers, type="scatter", marker="^", color="lightblue", markersize=70),
        ],
        volume=False,
        title="BTC-USD: Pivot Points (Market Structure)",
        savefig=os.path.join(output_dir, "08_pivot_points.png")
    )
    print("✓ Saved: outputs/08_pivot_points.png\n")
    
    # 9. ALL PATTERNS COMBINED
    print("=" * 60)
    print("9. ALL PATTERNS COMBINED VIEW")
    print("=" * 60)
    
    combined_plots = [
        mpf.make_addplot(hs_markers, type="scatter", marker="v", color="red", markersize=50),
        mpf.make_addplot(inv_hs_markers, type="scatter", marker="^", color="green", markersize=50),
        mpf.make_addplot(dt_markers, type="scatter", marker="X", color="darkred", markersize=60),
        mpf.make_addplot(db_markers, type="scatter", marker="X", color="darkgreen", markersize=60),
        mpf.make_addplot(support_line, color="green", width=1, linestyle=":", alpha=0.5),
        mpf.make_addplot(resistance_line, color="red", width=1, linestyle=":", alpha=0.5),
    ]
    
    mpf.plot(
        ohlc,
        type="candle",
        style="yahoo",
        addplot=combined_plots,
        volume=False,
        title="BTC-USD: All Major Patterns Combined",
        savefig=os.path.join(output_dir, "09_all_patterns_combined.png")
    )
    print("✓ Saved: outputs/09_all_patterns_combined.png\n")
    
    print("=" * 60)
    print("ALL PATTERN VISUALIZATIONS COMPLETED!")
    print("=" * 60)
    print("\nGenerated files in outputs/:")
    print("  1. 01_head_shoulder.png")
    print("  2. 02_double_top_bottom.png")
    print("  3. 03_multiple_tops_bottoms.png")
    print("  4. 04_triangle_patterns.png")
    print("  5. 05_wedge_patterns.png")
    print("  6. 06_channel_patterns.png")
    print("  7. 07_support_resistance.png")
    print("  8. 08_pivot_points.png")
    print("  9. 09_all_patterns_combined.png")

if __name__ == "__main__":
    main()

