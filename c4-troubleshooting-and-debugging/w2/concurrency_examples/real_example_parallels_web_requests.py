#!/usr/bin/env python3

import asyncio
import aiohttp


# Read more on: http://aiohttp.readthedocs.io/en/stable/


async def fetch(url):
    """Perform an HTTP GET to the URL and print the response"""
    response = await aiohttp.request('GET', url)
    return await response.text()

# Get a reference to the event loop
loop = asyncio.get_event_loop()

# Create the batch of requests we wish to execute
requests = [asyncio.ensure_future(fetch("https://github.com")),asyncio.ensure_future(fetch("https://google.com"))]

# Run the batch
responses = loop.run_until_complete(asyncio.gather(*requests))

# Examine responses
for resp in responses:
    print(resp)

""" Possible to interrupt:
try:
    loop.run_forever()
except KeyboardInterrupt:
    # Canceling pending tasks and stopping the loop
    asyncio.gather(*asyncio.Task.all_tasks()).cancel()
    # Stopping the loop
    loop.stop()
    # Received Ctrl+C
    loop.close()
"""
