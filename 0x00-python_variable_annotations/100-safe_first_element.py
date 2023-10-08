#!/usr/bin/env python3

"""This module contains a function for safely retrieving the first element of a sequence.
"""

from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieves the first element of a sequence if it exists.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

