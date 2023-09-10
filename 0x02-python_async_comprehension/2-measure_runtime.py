#!/usr/bin/env python3
"""
Measure Runtime Example

This module defines a coroutine called measure_runtime that executes async_comprehension four times in parallel using asyncio.gather and measures the total runtime.

Usage:
1. Run this module directly to measure the total runtime.
2. You can also import and use measure_runtime in other modules.

Example:
    $ python3 measure_runtime.py
"""

import asyncio
import time
from typing import List
from asyncio import run

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times in parallel.

    Returns:
        float: Total runtime in seconds.

    Usage:
        Call this coroutine to measure the runtime.
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    total_runtime = end_time - start_time

    return total_runtime

if __name__ == "__main__":
    total_runtime = run(measure_runtime())
    print(f"Total runtime: {total_runtime:.2f} seconds")

