#!/usr/bin/env python3

from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable of sequences.

    Args:
    - lst: An iterable of sequences (e.g., a list of strings).

    Returns:
    - A list of tuples, where each tuple contains a sequence (from the input iterable)
      and its corresponding length as an integer.
    """
    return [(i, len(i)) for i in lst]
