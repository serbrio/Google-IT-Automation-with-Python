#!/usr/bin/env python3

import time
import asyncio
from threading import Thread


#async def do_some_work(x):
#    print("waiting" + str(x))
#    await asyncio.sleep(x)


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
start_time = time.time()
t.start()
duration = time.time() - start_time
print("Duration: {} seconds".format(duration))
#loop = asyncio.get_event_loop()
#tasks = [asyncio.ensure_future(do_some_work(2)), asyncio.ensure_future(do_some_work(5))]
#loop.run_until_complete(asyncio.gather(*tasks))
