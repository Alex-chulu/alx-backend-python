#!/usr/bin/env python3

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Compute the length of each string in the given list.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where the first element
        is a string from the input list, and the second element is the
        length of that string.
    """
    return [(i, len(i)) for i in lst]

