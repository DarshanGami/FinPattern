# Trading Pattern Detection & Visualization

A comprehensive Python library for detecting and visualizing technical trading patterns in cryptocurrency and stock market data.

## 🌟 Features

- **9 Pattern Categories** detected automatically
- **Smart Pattern Filtering** using 3-stage algorithm
- **Professional Visualizations** with mplfinance
- **Clean Code Structure** with modular design
- **Extensible Framework** for adding custom patterns

## 📊 Detected Patterns

1. **Head & Shoulder** - Major reversal patterns
2. **Double Top/Bottom** - Strong reversal signals
3. **Multiple Tops/Bottoms** - Support/Resistance identification
4. **Triangle Patterns** - Continuation signals
5. **Wedge Patterns** - Potential reversals
6. **Channel Patterns** - Trend identification
7. **Support & Resistance** - Key price levels
8. **Pivot Points** - Market structure analysis
9. **Combined View** - All patterns together

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Quant.git
cd Quant

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from tradingpatterns import detect_head_shoulder, filter_best_patterns
import yfinance as yf

# Download data
df = yf.download("BTC-USD", period="6mo", interval="1d")
ohlc = df[["Open", "High", "Low", "Close"]]

# Detect patterns
result = detect_head_shoulder(ohlc, window=5)

# Filter best patterns
import numpy as np
hs_pos = np.where(result["head_shoulder_pattern"] == "Head and Shoulder")[0]
best_patterns = filter_best_patterns(hs_pos, ohlc)

print(f"Found {len(best_patterns)} significant Head & Shoulder patterns")
```

### Run Visualizations

```bash
# Activate virtual environment
source patscanx/bin/activate

# Generate Head & Shoulder chart only
python scripts/visualize_head_shoulder.py

# Generate all pattern charts (9 images)
python scripts/visualize_all_patterns.py
```

## 📁 Project Structure

```
Quant/
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── tradingpatterns/               # Core library package
│   ├── __init__.py               # Package initialization
│   ├── tradingpatterns.py        # Pattern detection algorithms
│   └── utils.py                  # Filtering utilities
├── scripts/                       # Visualization scripts
│   ├── visualize_head_shoulder.py
│   └── visualize_all_patterns.py
├── outputs/                       # Generated charts (created automatically)
│   ├── 01_head_shoulder.png
│   ├── 02_double_top_bottom.png
│   └── ... (9 images total)
├── docs/                          # Documentation
│   └── PATTERNS_GUIDE.md         # Pattern reference guide
├── data/                          # Data files
│   └── .gitkeep
└── patscanx/                      # Virtual environment
```

## 🔧 API Reference

### Pattern Detection Functions

```python
from tradingpatterns import (
    detect_head_shoulder,
    detect_double_top_bottom,
    detect_multiple_tops_bottoms,
    detect_triangle_pattern,
    detect_wedge,
    detect_channel,
    calculate_support_resistance,
    find_pivots
)

# All functions accept a DataFrame with OHLC columns
# Returns DataFrame with pattern column added
result = detect_head_shoulder(ohlc, window=5)
```

### Filtering Functions

```python
from tradingpatterns import (
    filter_best_patterns,
    filter_patterns_by_distance,
    cluster_and_select_best,
    filter_by_strength
)

# Main filtering function with 3-stage process
best = filter_best_patterns(
    positions,          # Array of pattern positions
    ohlc,              # OHLC DataFrame
    cluster_distance=10,  # Max distance for clustering
    min_distance=15,    # Min distance between patterns
    max_patterns=10     # Maximum patterns to return
)
```

## 🎨 Pattern Filtering Algorithm

The library uses a sophisticated 3-stage filtering process:

1. **Clustering** - Groups nearby patterns (within 10 bars)
2. **Distance** - Ensures minimum 15 bars between patterns
3. **Strength** - Selects top N patterns by price volatility

This eliminates noise and highlights only the most significant patterns.

## 📖 Documentation

- **[Pattern Guide](docs/PATTERNS_GUIDE.md)** - Detailed explanation of all patterns, symbols, and trading implications
- **API Docs** - See docstrings in source code
- **Examples** - Check scripts/ directory

## 🛠️ Development

### Adding New Patterns

1. Add detection function to `tradingpatterns/tradingpatterns.py`
2. Update `tradingpatterns/__init__.py` exports
3. Add visualization to scripts
4. Document in `docs/PATTERNS_GUIDE.md`

### Running Tests

```bash
# Activate environment
source patscanx/bin/activate

# Run pattern detection on sample data
python scripts/visualize_all_patterns.py
```

## 📦 Dependencies

- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `mplfinance` - Financial charting
- `yfinance` - Market data download
- `matplotlib` - Plotting backend

See `requirements.txt` for specific versions.

## 📝 License

MIT License - feel free to use in your projects!

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new patterns
4. Submit a pull request

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

## 🎯 Pattern Recognition Examples

### Head & Shoulder (Bearish)
```
     /\
    /  \    /\
   /    \  /  \
  /      \/    \
```

### Inverse Head & Shoulder (Bullish)
```
  \      /\    /
   \    /  \  /
    \  /    \/
     \/
```

### Double Top (Bearish)
```
   /\    /\
  /  \  /  \
 /    \/    \
```

### Support & Resistance
```
Price
  ^
  |  ---R---  (Resistance)
  |  /\/\/\
  |  ---S---  (Support)
  +----------> Time
```

---

**Happy Trading! 📈📉**

*Disclaimer: This tool is for educational purposes. Always perform your own analysis before making trading decisions.*
