#!/usr/bin/env python3

import asyncio
from typing import List

async def task_wait_random(max_delay: int) -> float:
    """
    Create an asyncio.Task that waits for a random delay between 0 and max_delay (inclusive).

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: A Task that waits for the random delay.
    """
    async def random_delay():
        await asyncio.sleep(uniform(0, max_delay))

    return asyncio.create_task(random_delay())

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times with specified max_delay and return a list of delays.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)
    return sorted([task.result() for task in tasks])

