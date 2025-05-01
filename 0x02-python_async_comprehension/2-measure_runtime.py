#!/usr/bin/env python3
"""
Module for measure_runtime coroutine.
This module provides a coroutine to measure the runtime of running
async_comprehension four times in parallel.
"""


import asyncio
import time

# import via __import__ to handle module name starting with a digit
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4 times in parallel, returns time in s."""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.time() - start


if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())
    print(runtime)
