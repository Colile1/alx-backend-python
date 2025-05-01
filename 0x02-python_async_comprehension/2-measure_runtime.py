#!/usr/bin/env python3
"""
Module contains a coroutine to measure the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather,
    measures the total runtime, and returns it.
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
