#2.1
'''import time
async def f(n):
    start = time.perf_counter()
    print(f"Task {n} started")
    await asyncio.sleep(round(random.uniform(0.2,0.5), 2))
    print(f"Task {n} finished")
    return time.perf_counter()-start


async def run_basic_group():
    result = []
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(f(1))
        t2 = tg.create_task(f(2))
        t3 = tg.create_task(f(3))


        result.append(await t1)
        result.append(await t2)
        result.append(await t3)
    print(result)

asyncio.run(run_basic_group())'''

#2.2
'''import asyncio
import random
async def f(n):
    print(f"Task {n} started")
    try:
        await asyncio.sleep(random.uniform(0.2, 3))
        if n == 2:
            raise ValueError('Ошибка')
    except asyncio.CancelledError:
        print(f"Task {n} cancelled")
        raise
    print(f"Task {n} finished")

async def  run_with_error():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(f(1))
            tg.create_task(f(2))
            tg.create_task(f(3))

    except* ValueError as eg:
        print("Ошибка:", eg.exceptions)

asyncio.run(run_with_error())'''

##2.3
'''
import asyncio
import random
import time

async def f(n):
    print(f"Task {n} started")
    await asyncio.sleep(round(random.uniform(0.2,0.5), 2))
    print(f"Task {n} finished")

class AsyncTimer:
    async def __aenter__(self):
        self.start = time.perf_counter()
        return self
    async def __aexit__(self, exc_type, exc, tb):
        exit_time = time.perf_counter() - self.start
        print(exit_time)

async def main():
    async with AsyncTimer():
        async with asyncio.TaskGroup() as tg:
            tg.create_task(f(1))
            tg.create_task(f(2))

asyncio.run(main())'''

##2.4
'''
import asyncio
import random

async def async_range(n):
    for i in range(n):
        await asyncio.sleep(random.uniform(0.2,1.2))
        yield i
        
async def f():
    for i in range(20):
        print("в работе")
        await asyncio.sleep(0.5)

async def main():
    t1 = asyncio.create_task(f())
    async for i in async_range(6):
        print(i)
    await t1
asyncio.run(main())'''