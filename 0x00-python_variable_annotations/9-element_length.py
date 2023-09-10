#!/usr/bin/env python3

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of each element in the input list.

    Args:
    - lst: A list of strings.

    Returns:
    - A list of tuples, where each tuple contains a string from the input list
      and its corresponding length.
    """
    return [(i, len(i)) for i in lst]

