#!/usr/bin/env python3

"""
Module: my_module
This module provides a function for obtaining the first element of an iterable.
"""

from typing import Iterable, Any

def safe_first_element(lst: Iterable[Any]) -> Any:
    """
    Get the first element of an iterable if it exists.

    Args:
        lst (Iterable[Any]): An iterable of elements.

    Returns:
        Any: The first element of the iterable, or None if the iterable is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
