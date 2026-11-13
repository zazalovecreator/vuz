import asyncio
import random
##1
'''
async def f1():
    print('поставил варить макароны')
    await asyncio.sleep(0.5)
    return 'макароны готовы'

async def f2():
    print('режу салат')
    await asyncio.sleep(0.5)
    print('салат готов')

async def main():
    task = asyncio.create_task(f1())
    task2 = asyncio.create_task(f2())
    y = await task
    print(y)
    await task2
asyncio.run(main())'''

##2
##список с некоторыми четными и не четными числами
##алгоритм проверяет какое-то число на не четность

'''spisok = [1,3,5,7,9,11,2,4,6,8]

async def prov_na_nechetn():
    x = random.randint(0,9)
    await asyncio.sleep(0.5)
    if spisok[x]%2==0:
        raise ValueError(f"{spisok[x]} четное")
    return f"все супер, {spisok[x]} не четное"


async def main():
    print('проверка четности числа из spisok')
    t = asyncio.create_task(prov_na_nechetn())
    print("статус до await", t.done())

    try:
        await t
        print("статус после await", t.done())
        print(t.result())
    except ValueError:
        print("статус после await",t.done())
        print("ошибка:", t.exception())

asyncio.run(main())'''



##3
'''
async def zadacha():
    print("я задача:", asyncio.current_task().get_name())
    await asyncio.sleep(0.1)
    print("я задача:", asyncio.current_task().get_name())


async def main():
    t1 = asyncio.create_task(zadacha(), name="кошка")
    t2 = asyncio.create_task(zadacha(), name='собака')
    t3 = asyncio.create_task(zadacha(), name='лиса')
    await asyncio.sleep(0.05)
    print("переименовал")
    t3.set_name("abrams m1")
    await t1
    await t2
    await t3
asyncio.run(main())'''


###4

'''async def zadacha(delay):
    await asyncio.sleep(delay)

async def main():
    asyncio.current_task().set_name("main")
    asyncio.create_task(zadacha(3), name = "машина")
    asyncio.create_task(zadacha(1), name = "вертолет")
    asyncio.create_task(zadacha(0.6), name="самолет")
    asyncio.create_task(zadacha(2), name="мотоцикл")
    while len(asyncio.all_tasks())!=1:
        print(len(asyncio.all_tasks()))
        print([t.get_name() for t in asyncio.all_tasks()])
        await asyncio.sleep(0.4)

asyncio.run(main())'''

##5
'''
async def f():
    for i in range(15):
        await asyncio.sleep(0.2)
        print("работа")
    return "выполнено"

async def main():
    t = asyncio.create_task(f())
    await asyncio.sleep(1)
    t.cancel()
    try:
        await t
        print(t.result())
    except asyncio.CancelledError:
        print("задача отменена:", t.cancelled())
        print("задача закончена:", t.done())

asyncio.run(main())'''



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

asyncio.run(run_with_error())