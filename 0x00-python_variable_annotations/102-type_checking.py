#!/usr/bin/env python3

"""
Zoom Array Module
"""

from typing import List, Tuple

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in on an array by repeating each element.

    Args:
        lst (List[int]): The input list.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List[int]: The zoomed-in list.
    """
    zoomed_in = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

if __name__ == "__main__":
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)
    print(zoom_2x)

    zoom_3x = zoom_array(array, 3)
    print(zoom_3x)

