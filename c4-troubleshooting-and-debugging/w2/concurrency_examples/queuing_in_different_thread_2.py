#!/usr/bin/env python3

import time
import asyncio
from threading import Thread


async def do_some_work(x):
    print("waiting" + str(x))
    await asyncio.sleep(x)


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    print("More work {}".format(x))
    time.sleep(x)
    print("Finished more work {}".format(x))


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
start_time = time.time()
#t.start()
new_loop.call_soon_threadsafe(more_work, 20)
asyncio.run_coroutine_threadsafe(do_some_work(5), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(10), new_loop)
duration = time.time() - start_time
print("Duration: {} seconds".format(duration))
#loop = asyncio.get_event_loop()
#tasks = [asyncio.ensure_future(do_some_work(2)), asyncio.ensure_future(do_some_work(5))]
#loop.run_until_complete(asyncio.gather(*tasks))
