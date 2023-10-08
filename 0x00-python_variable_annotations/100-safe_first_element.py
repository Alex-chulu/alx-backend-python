#!/usr/bin/env python3

from typing import List, Any, Union

def safe_first_element(lst: List[Any]) -> Union[None, Any]:
    """
    Safely retrieve the first element of a list if it exists.

    Args:
        lst (List[Any]): A list of elements of any type.

    Returns:
        Union[None, Any]: The first element of the list if it exists, else None.
    """
    if lst:
        return lst[0]
    else:
        return None

