import aiohttp
import asyncio
import time

start_time = time.time()
session = aiohttp.ClientSession()

async def get(url):
    async with session.get(url) as response:
        return await response.json()
