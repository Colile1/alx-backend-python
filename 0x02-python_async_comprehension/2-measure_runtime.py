#!/usr/bin/env python3
"""
Module for measure_runtime coroutine.
This module provides a coroutine to measure the runtime of running async_comprehension four times in parallel.
"""
import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension four times in parallel.
    Returns the elapsed time in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
