#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
from typing import List
from random import random

async def async_generator() -> float:
    '''Asynchronous generator that yields 10 random numbers.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 100

async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using async comprehensions.'''
    return [rand async for rand in async_generator()]

# Example usage:
async def main():
    '''Main coroutine to run async_comprehension.'''
    random_numbers = await async_comprehension()
    print(random_numbers)

if __name__ == "__main__":
    asyncio.run(main())

