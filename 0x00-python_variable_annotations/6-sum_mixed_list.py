#!/usr/bin/env python3

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
    - mxd_lst: A list of integers and floats.

    Returns:
    - The sum of the integers and floats in the input list as a float.
    """
    return float(sum(mxd_lst))
