#!/usr/bin/env python3

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n(n, max_delay).

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay for each wait_n call.

    Returns:
        float: Average execution time in seconds.
    """
    start_time = time.time()

    loop = asyncio.get_event_loop()
    delays = loop.run_until_complete(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n

if __name__ == '__main__':
    n = 5
    max_delay = 2
    avg_time = measure_time(n, max_delay)
    print(f"Average execution time for {n} calls with max delay {max_delay}: {avg_time} seconds")
