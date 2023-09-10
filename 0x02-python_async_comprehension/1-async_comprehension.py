#!/usr/bin/env python3
"""
Async Comprehension Example

This module defines an asynchronous coroutine called async_comprehension that collects 10 random numbers using an async comprehension over async_generator.

Usage:
1. Run this module directly to see the collected random numbers.
2. You can also import and use async_comprehension in other modules.

Example:
    $ python3 async_comprehension.py
"""

from typing import List
from asyncio import run

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[int]:
    """
    Collect 10 random numbers asynchronously using an async comprehension.

    Returns:
        List[int]: A list of 10 random numbers.

    Usage:
        Call this coroutine to get the list of random numbers.
    """
    return [number async for number in async_generator()]

if __name__ == "__main__":
    collected_numbers = run(async_comprehension())
    print(collected_numbers)

