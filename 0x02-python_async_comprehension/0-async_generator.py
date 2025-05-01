#!/usr/bin/env python3
"""
Module for async_generator coroutine.

This module provides a coroutine that yields random numbers asynchronously.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield a random float between 0 and 10, 10 times, waiting 1
    second each time.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
