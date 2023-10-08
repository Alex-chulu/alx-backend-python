#!/usr/bin/env python3

"""This module contains a function for computing the length of sequences in an iterable.
"""

from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of sequences in an iterable.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence from the input
        iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]

