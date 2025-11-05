# Project Structure

This document explains the organization and purpose of each directory and file in the Trading Pattern Detection project.

## 📂 Directory Tree

```
Quant/
│
├── 📄 README.md                           # Project overview and quick start guide
├── 📄 requirements.txt                     # Python package dependencies
├── 📄 .gitignore                          # Git ignore rules
├── 📄 run_analysis.py                     # Main interactive runner script
├── 📄 temp.py                             # Temporary/scratch file (gitignored)
│
├── 📁 tradingpatterns/                    # Core library package
│   ├── 📄 __init__.py                     # Package initialization & exports
│   ├── 📄 tradingpatterns.py              # Pattern detection algorithms
│   └── 📄 utils.py                        # Filtering & utility functions
│
├── 📁 scripts/                            # Executable visualization scripts
│   ├── 📄 visualize_head_shoulder.py      # H&S pattern visualization
│   └── 📄 visualize_all_patterns.py       # All patterns comprehensive view
│
├── 📁 outputs/                            # Generated charts & visualizations
│   ├── 📄 .gitkeep                        # Keeps directory in git
│   ├── 🖼️  01_head_shoulder.png           # Generated chart files
│   ├── 🖼️  02_double_top_bottom.png
│   ├── 🖼️  03_multiple_tops_bottoms.png
│   ├── 🖼️  04_triangle_patterns.png
│   ├── 🖼️  05_wedge_patterns.png
│   ├── 🖼️  06_channel_patterns.png
│   ├── 🖼️  07_support_resistance.png
│   ├── 🖼️  08_pivot_points.png
│   └── 🖼️  09_all_patterns_combined.png
│
├── 📁 docs/                               # Documentation files
│   ├── 📄 PATTERNS_GUIDE.md               # Pattern reference & trading guide
│   └── 📄 PROJECT_STRUCTURE.md            # This file
│
├── 📁 data/                               # Data files directory
│   ├── 📄 .gitkeep                        # Keeps directory in git
│   └── 📊 btc_2y.csv                      # Sample data (gitignored if added)
│
└── 📁 patscanx/                           # Python virtual environment (gitignored)
    ├── bin/                               # Executable files
    ├── lib/                               # Installed packages
    └── pyvenv.cfg                         # venv configuration
```

---

## 📋 File Descriptions

### Root Level Files

#### `README.md`
- **Purpose**: Project documentation homepage
- **Contains**: Features, installation, usage examples, API reference
- **Audience**: New users and contributors

#### `requirements.txt`
- **Purpose**: Python package dependencies
- **Usage**: `pip install -r requirements.txt`
- **Contains**: pandas, numpy, mplfinance, yfinance, matplotlib

#### `.gitignore`
- **Purpose**: Specifies files/directories Git should ignore
- **Ignores**: Virtual env, outputs, cache files, temp files

#### `run_analysis.py`
- **Purpose**: Interactive command-line interface
- **Features**: Menu-driven pattern analysis execution
- **Usage**: `python run_analysis.py`

---

## 📦 Package: `tradingpatterns/`

The core library containing all pattern detection logic.

### `__init__.py`
- **Purpose**: Makes directory a Python package
- **Exports**: All detection functions and utilities
- **Usage**: `from tradingpatterns import detect_head_shoulder`

### `tradingpatterns.py`
- **Purpose**: Core pattern detection algorithms
- **Contains**:
  - `detect_head_shoulder()` - H&S pattern detection
  - `detect_double_top_bottom()` - Double patterns
  - `detect_multiple_tops_bottoms()` - Multiple tests
  - `detect_triangle_pattern()` - Triangle formations
  - `detect_wedge()` - Wedge patterns
  - `detect_channel()` - Channel trends
  - `calculate_support_resistance()` - S&R levels
  - `find_pivots()` - Market structure pivots
- **Input**: OHLC DataFrame
- **Output**: DataFrame with pattern column

### `utils.py`
- **Purpose**: Pattern filtering and helper functions
- **Contains**:
  - `filter_best_patterns()` - Main 3-stage filtering
  - `filter_patterns_by_distance()` - Distance-based filter
  - `cluster_and_select_best()` - Clustering algorithm
  - `filter_by_strength()` - Strength-based selection
- **Usage**: Clean up noisy pattern detections

---

## 🎬 Scripts: `scripts/`

Executable scripts for generating visualizations.

### `visualize_head_shoulder.py`
- **Purpose**: Generate Head & Shoulder pattern chart
- **Output**: `outputs/head_shoulder_patterns.png`
- **Runtime**: ~10-15 seconds
- **Usage**: `python scripts/visualize_head_shoulder.py`

### `visualize_all_patterns.py`
- **Purpose**: Generate all 9 pattern charts
- **Output**: 9 PNG files in `outputs/`
- **Runtime**: ~30-45 seconds
- **Features**:
  - Progress indicators
  - Pattern statistics
  - Automatic error handling
- **Usage**: `python scripts/visualize_all_patterns.py`

---

## 🖼️ Outputs: `outputs/`

Generated chart images directory.

### File Naming Convention
```
{number}_{pattern_name}.png
```

### Generated Files
1. `01_head_shoulder.png` - Bearish/Bullish H&S
2. `02_double_top_bottom.png` - Double patterns
3. `03_multiple_tops_bottoms.png` - Support/Resistance tests
4. `04_triangle_patterns.png` - Ascending/Descending triangles
5. `05_wedge_patterns.png` - Rising/Falling wedges
6. `06_channel_patterns.png` - Up/Down channels
7. `07_support_resistance.png` - S&R levels
8. `08_pivot_points.png` - HH/LL/HL/LH markers
9. `09_all_patterns_combined.png` - Comprehensive view

**Note**: These files are gitignored. Generate fresh on each system.

---

## 📚 Documentation: `docs/`

Comprehensive documentation files.

### `PATTERNS_GUIDE.md`
- **Purpose**: Complete pattern reference
- **Contains**:
  - Pattern descriptions
  - Symbol/color legends
  - Trading implications
  - Strategy tips
- **Audience**: Traders and analysts

### `PROJECT_STRUCTURE.md`
- **Purpose**: This file
- **Contains**: Project organization explanation
- **Audience**: Developers and contributors

---

## 📊 Data: `data/`

Data files directory (optional).

- **Purpose**: Store CSV and market data files
- **Usage**: Can store downloaded historical data
- **Note**: CSV files are gitignored to save space

---

## 🐍 Virtual Environment: `patscanx/`

Python virtual environment (gitignored).

- **Purpose**: Isolated Python environment
- **Activation**: `source patscanx/bin/activate`
- **Deactivation**: `deactivate`
- **Recreation**: `python3 -m venv patscanx`

---

## 🔄 Workflow

### Typical Usage Flow

```
1. Activate Environment
   └─> source patscanx/bin/activate

2. Run Analysis
   ├─> Option A: python run_analysis.py (Interactive)
   ├─> Option B: python scripts/visualize_head_shoulder.py (Direct)
   └─> Option C: python scripts/visualize_all_patterns.py (Comprehensive)

3. View Outputs
   └─> Open outputs/*.png files

4. Reference Documentation
   └─> Read docs/PATTERNS_GUIDE.md
```

### Development Workflow

```
1. Edit Core Logic
   └─> Modify tradingpatterns/tradingpatterns.py

2. Update Utilities
   └─> Modify tradingpatterns/utils.py

3. Test Changes
   └─> Run scripts to verify

4. Update Documentation
   ├─> Update README.md
   ├─> Update docs/PATTERNS_GUIDE.md
   └─> Update this file if structure changes

5. Commit Changes
   └─> git add, commit, push
```

---

## 🎯 Design Principles

### 1. **Separation of Concerns**
- **Core library** (`tradingpatterns/`) - Pure detection logic
- **Scripts** (`scripts/`) - Visualization & execution
- **Documentation** (`docs/`) - User guides

### 2. **Clean Outputs**
- All generated files go to `outputs/`
- Gitignored to keep repo clean
- Consistent naming convention

### 3. **Modularity**
- Each pattern has its own detection function
- Utilities are reusable across patterns
- Easy to extend with new patterns

### 4. **User-Friendly**
- Interactive runner script
- Clear documentation
- Sensible defaults

---

## 🚀 Adding New Features

### Adding a New Pattern

1. **Implement detection**:
   ```python
   # In tradingpatterns/tradingpatterns.py
   def detect_new_pattern(df, window=3):
       # Detection logic
       return df
   ```

2. **Export function**:
   ```python
   # In tradingpatterns/__init__.py
   from .tradingpatterns import detect_new_pattern
   __all__ = [..., 'detect_new_pattern']
   ```

3. **Create visualization**:
   ```python
   # In scripts/visualize_new_pattern.py
   from tradingpatterns import detect_new_pattern
   # Visualization code
   ```

4. **Document**:
   - Add to `docs/PATTERNS_GUIDE.md`
   - Update `README.md`

---

## 📝 Best Practices

1. **Keep tradingpatterns/ clean** - Only detection logic
2. **Put all outputs in outputs/** - Don't scatter files
3. **Document all functions** - Use docstrings
4. **Use consistent naming** - Follow existing patterns
5. **Test before committing** - Run full analysis

---

**Last Updated**: November 2025

