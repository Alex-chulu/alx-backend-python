#!/usr/bin/env python3
"""Create a asyncio.Task with wait_random from 0-basic_async_syntax."""

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task for wait_random with the given max_delay."""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))


if __name__ == "__main__":
    random.seed(1)
    task = task_wait_random(5)
    asyncio.run(task)

