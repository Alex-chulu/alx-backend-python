#!/usr/bin/env python3
"""
Zooms in on an array by repeating its elements by a factor
"""
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Zooms in on an array by repeating its elements by a factor.

    Args:
        lst (Tuple[int, ...]): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List[int]: The zoomed-in array.
    """
    zoomed_in: List[int] = [
        x for x in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)

