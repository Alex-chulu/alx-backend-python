#!/usr/bin/env python3

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string k and the square of the int/float v.

    Args:
    - k: A string.
    - v: An integer or a float.

    Returns:
    - A tuple containing the string k and the square of v as a float.
    """
    return (k, float(v ** 2))
