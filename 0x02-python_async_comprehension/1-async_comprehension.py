#!/usr/bin/env python3
"""
Async Comprehension Example

This module defines an asynchronous coroutine called async_comprehension 
that collects 10 random numbers using an async comprehension over async_generator.

Usage:
1. Run this module directly to see the collected random numbers.
2. You can also import and use async_comprehension in other modules.

Example:
    $ python3 async_comprehension.py
"""
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine will collect random numbers using an async
    comprehensing"""
    return [y async for y in async_generator()]
