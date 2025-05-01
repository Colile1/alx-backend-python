#!/usr/bin/env python3
"""
Module for async_generator coroutine.

This module provides a coroutine that yields random numbers asynchronously.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yields 10 random floats between 0 and 10, 10s apart."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
