"""Utility functions for pattern filtering and analysis"""

import numpy as np
import pandas as pd


def filter_patterns_by_distance(positions, min_distance=15):
    """
    Keep only patterns separated by min_distance bars
    
    Args:
        positions: Array of pattern positions
        min_distance: Minimum number of bars between patterns
        
    Returns:
        Filtered array of positions
    """
    if len(positions) == 0:
        return positions
    
    filtered = [positions[0]]
    for pos in positions[1:]:
        if pos - filtered[-1] >= min_distance:
            filtered.append(pos)
    return np.array(filtered)


def cluster_and_select_best(positions, ohlc, cluster_distance=10):
    """
    Cluster nearby patterns and select best from each cluster
    
    Args:
        positions: Array of pattern positions
        ohlc: DataFrame with OHLC data
        cluster_distance: Maximum distance between patterns in same cluster
        
    Returns:
        Array of best positions from each cluster
    """
    if len(positions) == 0:
        return positions
    
    clusters = []
    current_cluster = [positions[0]]
    
    for pos in positions[1:]:
        if pos - current_cluster[-1] <= cluster_distance:
            current_cluster.append(pos)
        else:
            clusters.append(current_cluster)
            current_cluster = [pos]
    clusters.append(current_cluster)
    
    # Select best from each cluster (highest range)
    best_positions = []
    for cluster in clusters:
        ranges = [ohlc['High'].iloc[p] - ohlc['Low'].iloc[p] for p in cluster]
        best_idx = np.argmax(ranges)
        best_positions.append(cluster[best_idx])
    
    return np.array(best_positions)


def filter_by_strength(positions, ohlc, top_n=10):
    """
    Select top_n strongest patterns by price range
    
    Args:
        positions: Array of pattern positions
        ohlc: DataFrame with OHLC data
        top_n: Maximum number of patterns to return
        
    Returns:
        Array of top N strongest positions
    """
    if len(positions) == 0 or len(positions) <= top_n:
        return positions
    
    strengths = []
    for pos in positions:
        strength = ohlc['High'].iloc[pos] - ohlc['Low'].iloc[pos]
        strengths.append((pos, strength))
    
    # Sort by strength and take top_n
    strengths.sort(key=lambda x: x[1], reverse=True)
    filtered = np.array([s[0] for s in strengths[:top_n]])
    return np.sort(filtered)  # Re-sort by time


def filter_best_patterns(positions, ohlc, cluster_distance=10, min_distance=15, max_patterns=10):
    """
    Multi-stage filtering to select the best patterns:
    1. Cluster nearby patterns and select best from each cluster
    2. Ensure minimum distance between patterns
    3. Limit to top N strongest patterns
    
    Args:
        positions: Array of pattern positions
        ohlc: DataFrame with OHLC data
        cluster_distance: Maximum distance for clustering
        min_distance: Minimum distance between final patterns
        max_patterns: Maximum number of patterns to return
        
    Returns:
        Array of filtered positions
    """
    if len(positions) == 0:
        return positions
    
    # Stage 1: Cluster and select best from each
    filtered = cluster_and_select_best(positions, ohlc, cluster_distance)
    
    # Stage 2: Ensure minimum distance
    filtered = filter_patterns_by_distance(filtered, min_distance)
    
    # Stage 3: Limit to top N strongest
    if len(filtered) > max_patterns:
        filtered = filter_by_strength(filtered, ohlc, max_patterns)
    
    return filtered

