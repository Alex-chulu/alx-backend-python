#!/usr/bin/env python3

"""
This module defines a function for safely retrieving the first element of an iterable.
"""

from typing import Iterable, Any

def safe_first_element(lst: Iterable[Any]) -> Any:
    """
    Safely retrieves the first element of an iterable.

    Args:
        lst (Iterable[Any]): An iterable of elements of any type.

    Returns:
        Any: The first element of the iterable, or None if the iterable is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

