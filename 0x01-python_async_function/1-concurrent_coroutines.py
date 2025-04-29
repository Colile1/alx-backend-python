#!/usr/bin/env python3
"""Module for spawning multiple wait_random coroutines and
returning their delays in order.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with max_delay and returns list of
    delays in ascending order.
    """
    delays: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
