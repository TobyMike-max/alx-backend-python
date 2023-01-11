#!/usr/bin/env python3
"""A basic async function"""
import random
import asyncio


async def wait_random(delay: int = 10) -> float:
    """An async function that sleeps within a random float
    Input:
        delay(int): Defaults to 10
    Return:
        delay(float)
    """
    delay = random.uniform(0, delay)
    await asyncio.sleep(delay)
    return delay