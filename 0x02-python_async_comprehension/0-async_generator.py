#!/usr/bin/env python3
"""
Async Generator Example

This module defines an asynchronous generator called async_generator, which generates random numbers between 0 and 10 with a 1-second delay between each value.

Usage:
1. Run this module directly to see the generated values.
2. You can also import and use async_generator in other modules.

Example:
    $ python3 async_generator.py
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None]:
    """
    Generate random numbers between 0 and 10 asynchronously.

    Yields:
        int: A random number between 0 and 10.

    Usage:
        Use an asynchronous for loop to iterate through the values produced by this generator.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

async def main():
    """
    Main function to demonstrate the usage of async_generator.
    """
    async for number in async_generator():
        print(number)

if __name__ == "__main__":
    asyncio.run(main())

