#!/usr/bin/env python3
"""A basic async function"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An async function that sleeps within a random float
    Input:
        delay(int): Defaults to 10
    Return:
        delay(float)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
