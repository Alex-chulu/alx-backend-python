#!/usr/bin/env python3
'''Task 12's module.
'''
from typing import Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    '''Zooms in on an array by repeating its elements by a factor.
    Args:
        lst (Tuple[int, ...]): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple[int, ...]: The zoomed-in array.
    '''
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

