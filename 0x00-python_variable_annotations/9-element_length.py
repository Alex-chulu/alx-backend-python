#!/usr/bin/env python3

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of each element in the input list and return a list
    of tuples containing each element and its corresponding length.

    Args:
        lst (List[str]): The list of strings to calculate lengths for.

    Returns:
        List[Tuple[str, int]]: A list of tuples where the first element is a
        string from the input list, and the second element is its length.

    Example:
        >>> element_length(["apple", "banana", "cherry"])
        [('apple', 5), ('banana', 6), ('cherry', 6)]
    """
    return [(i, len(i)) for i in lst]

