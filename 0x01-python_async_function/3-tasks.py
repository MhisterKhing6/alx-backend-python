#!/usr/bin/env python3

'''
Creat a regular function that return a wait_random caroutin task
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    task_wait_random : returns asyncio.Task object
    Arguements:
        max_delay: The maximum time the funcion shoud sleed
        n : The number of caro rutines
    """
    return asyncio.current_task(wait_random(max_delay))
