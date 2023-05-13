#!/usr/bin/env python
import asyncio
from typing import Iterable
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterable[float]:
    result = [i async for i in async_generator()]
    return result
