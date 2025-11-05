"""Trading Pattern Detection Package"""

from .tradingpatterns import (
    detect_head_shoulder,
    detect_multiple_tops_bottoms,
    calculate_support_resistance,
    detect_triangle_pattern,
    detect_wedge,
    detect_channel,
    detect_double_top_bottom,
    detect_trendline,
    find_pivots
)

from .utils import (
    filter_patterns_by_distance,
    cluster_and_select_best,
    filter_by_strength,
    filter_best_patterns
)

__all__ = [
    # Pattern detection functions
    'detect_head_shoulder',
    'detect_multiple_tops_bottoms',
    'calculate_support_resistance',
    'detect_triangle_pattern',
    'detect_wedge',
    'detect_channel',
    'detect_double_top_bottom',
    'detect_trendline',
    'find_pivots',
    # Utility functions
    'filter_patterns_by_distance',
    'cluster_and_select_best',
    'filter_by_strength',
    'filter_best_patterns'
]

