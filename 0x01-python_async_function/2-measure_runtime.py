#!/usr/bin/env python3
"""
Measure the runtime of wait_n and calculate average time.
"""

import asyncio
import random
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n(n, max_delay).

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for wait_n.

    Returns:
        float: The average execution time in seconds.
    """
    start_time = time.time()

    async def run_wait_n():
        await wait_n(n, max_delay)

    asyncio.run(run_wait_n())

    total_time = time.time() - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 5
    avg_time = measure_time(n, max_delay)
    print(f"Average time for wait_n({n}, {max_delay}): {avg_time:.2f} seconds")

