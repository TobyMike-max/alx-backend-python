#!/usr/bin/env python3
"""Execute multiple coroutines at same time with async"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that returns a list of delays in ascending order
    Args:
        n(int): Number of times to spawn wait_random function
        max_delay(int): Maximum time for wait random argument.
    Return:
        finish(List[float])
    """
    tsk_obj = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(tsk_obj)]
    return finish
