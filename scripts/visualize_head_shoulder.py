"""
Head & Shoulder Pattern Visualization Script
Detects and visualizes Head & Shoulder and Inverse Head & Shoulder patterns
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

from tradingpatterns import detect_head_shoulder, filter_best_patterns

def main():
    # Output directory
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
    
    # Detect patterns
    work = detect_head_shoulder(ohlc.reset_index(drop=True).copy(), window=5)
    hs_pos = np.where(work["head_shoulder_pattern"] == "Head and Shoulder")[0]
    inv_pos = np.where(work["head_shoulder_pattern"] == "Inverse Head and Shoulder")[0]
    
    # Apply filtering to get best patterns
    hs_pos = filter_best_patterns(hs_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    inv_pos = filter_best_patterns(inv_pos, ohlc, cluster_distance=10, min_distance=15, max_patterns=10)
    
    # Create marker series
    hs_markers = pd.Series(np.nan, index=ohlc.index)
    hs_markers.iloc[hs_pos] = ohlc["High"].iloc[hs_pos]
    inv_markers = pd.Series(np.nan, index=ohlc.index)
    inv_markers.iloc[inv_pos] = ohlc["Low"].iloc[inv_pos]
    
    # Plot
    print(f"✓ Found {len(hs_pos)} Head & Shoulder patterns")
    print(f"✓ Found {len(inv_pos)} Inverse Head & Shoulder patterns")
    
    output_path = os.path.join(output_dir, 'head_shoulder_patterns.png')
    mpf.plot(
        ohlc,
        type="candle",
        style="yahoo",
        addplot=[
            mpf.make_addplot(hs_markers, type="scatter", marker="v", color="red", markersize=50),
            mpf.make_addplot(inv_markers, type="scatter", marker="^", color="green", markersize=50),
        ],
        volume=False,
        title="BTC-USD: Head & Shoulder Pattern Detection (Filtered Best Patterns)",
        savefig=output_path
    )
    
    print(f"\n✓ Chart saved to: {output_path}")

if __name__ == "__main__":
    main()

