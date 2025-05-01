#!/usr/bin/env python3
"""
Module contains a coroutine using async comprehension.
"""

import asyncio
from typing import List

# Correctly import async_generator from the specified module file name
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an async comprehension and returns them.
    """
    result = [i async for i in async_generator()]
    return result
