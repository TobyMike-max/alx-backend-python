#!/usr/bin/env python3
"""Execute multiple coroutines at same time with async"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, delay: int) -> List[float]:
    """Function that returns a list of delays in ascending order
    Args:
        n(int): Number of times to spawn wait_random function
        delay(int): Maximum time for wait random argument.
    Return:
        finish(List[float])
    """
    tsk_obj = [task_wait_random(delay) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(tsk_obj)]
    return finish
