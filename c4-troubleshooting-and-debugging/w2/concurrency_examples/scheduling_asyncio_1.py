#!/usr/bin/env python3

import time
import asyncio

async def do_some_work(x):
    print("waiting" + str(x))
    await asyncio.sleep(x)

loop = asyncio.get_event_loop()
start_time = time.time()
loop.run_until_complete(do_some_work(5))
duration = time.time() - start_time
print("Duration: {} seconds".format(duration))
