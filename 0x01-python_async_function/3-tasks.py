#!/usr/bin/env python3
"""Asyncio and regular function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Regular function that returns a asyncio.Task
    Args:
        max_delay(int): Maximum delay value
    Return:
        asyncio.Task
    """
    end = asyncio.create_task(wait_random(max_delay))
    return end
