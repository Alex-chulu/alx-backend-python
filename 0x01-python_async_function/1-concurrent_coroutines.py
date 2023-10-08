#!/usr/bin/env python3
"""Asynchronous Python code."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` `n` times with specified `max_delay`.

    Args:
        n (int): The number of times to call `wait_random`.
        max_delay (int): The maximum delay for `wait_random`.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []

    async def gather_delays(i: int):
        """
        Gather delays from `wait_random`.

        Args:
            i (int): The index of the current call.
        """
        delay = await wait_random(max_delay)
        delays.append(delay)
        if len(delays) == n:
            delays.sort()

    await asyncio.gather(*(gather_delays(i) for i in range(n)))

    return delays

if __name__ == "__main__":
    n = 5
    max_delay = 5
    print(asyncio.run(wait_n(n, max_delay)))

