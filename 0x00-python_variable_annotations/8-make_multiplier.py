#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies a float by the given multiplier.

    Args:
    - multiplier: A float.

    Returns:
    - A function that takes a float and returns the result of multiplying it by multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function

