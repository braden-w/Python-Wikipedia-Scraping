import asyncio
from time import sleep
from collections import deque


# def countto3():
#     print(1)
#     sleep(1)
#     print(2)
#     sleep(1)
#     print(3)


# async def asynccountto3():
#     loop = asyncio.get_event_loop()
#     print(1)
#     loop.run_in_executor(None, sleep, 1)
#     print(2)
#     loop.run_in_executor(None, sleep, 1)
#     print(3)


# def timer(function):
#     start = time.perf_counter()
#     asyncio
#     end = time.perf_counter()
#     elapsed = end - start


# countto3()
# asyncio.run(asynccountto3())


queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


async def process_queue_time(first_queue):
    if first_queue % 2 == 0:
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
    return first_queue


async def approach_2():
    loop = asyncio.get_event_loop()
    while queue[0] != 10:
        ret = await process_queue_time(queue.popleft())
        print(ret)


def approach_1():
    while queue[0] != 10:
        print(process_queue_time(queue.popleft()))


# approach_1()
asyncio.run(approach_2())