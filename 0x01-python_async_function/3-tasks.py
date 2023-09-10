#!/usr/bin/env python3

import asyncio
from random import uniform

def wait_random(max_delay: int) -> asyncio.Task:
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

# Example usage:
if __name__ == "__main__":
    max_delay = 5
    task = wait_random(max_delay)
    asyncio.run(task)  # Run the task in an asyncio event loop

