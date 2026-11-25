import asyncio
import random

##1 FIFO
'''queue = asyncio.Queue()

async def client(col):

    lst = []
    count = 1
    for i in range(col):
        lst.append(f'Запрос №{count}')
        count += 1

    for request in lst:
        await asyncio.sleep(random.uniform(0.5,1))
        await queue.put(request)
        print(f'{request} в очереди')


async def server(queue, col):
    for i in range(col):
        request = await queue.get()
        print(f'{request} в обработке')
        await asyncio.sleep(random.uniform(1,2))
        print(f'Cервер закончил обработку {request}')
        queue.task_done()

async def main():
    col = int(input('Введи количество запросов:'))
    await asyncio.gather(client(col), server(queue, col))
    print("---------------------------------------------------------------"
          "-------------------------------------------")
    print("Все запросы обработаны")


asyncio.run(main())'''


##2 LIFO
'''
queue = asyncio.LifoQueue()
async def client(col):

    lst = []
    count = 1
    for i in range(col):
        lst.append(f'Запрос №{count}')
        count += 1

    for request in lst:
        await asyncio.sleep(random.uniform(0.5,1))
        await queue.put(request)
        print(f'{request} в очереди')

async def server(queue, col):
    for i in range(col):
        request = await queue.get()
        print(f'{request} в обработке')
        await asyncio.sleep(random.uniform(2,3))
        print(f'Cервер закончил обработку {request}')
        queue.task_done()

async def main():
    col = int(input('Введи количество запросов:'))
    await asyncio.gather(client(col), server(queue, col))
    print("---------------------------------------------------------------"
          "-------------------------------------------")
    print("Все запросы обработаны")


asyncio.run(main())
'''

##3 PriorityQueue

queue = asyncio.PriorityQueue()
async def client(col):
    lst = []
    count = 1
    for i in range(col):
        inp = int(input(f'Введи приоритет Запроса №{count}:'))
        item = f'Запрос №{count}'
        lst.append((inp,item))
        count+=1

    for request in lst:
        await asyncio.sleep(random.uniform(0.5,1))
        await queue.put(request)
        print(f'{request} в очереди')

async def server(queue, col):
    for i in range(col):
        request = await queue.get()
        print(f'{request} в обработке')
        await asyncio.sleep(random.uniform(2,3))
        print(f'Cервер закончил обработку {request}')
        queue.task_done()

async def main():
    col = int(input('Введи количество запросов:'))
    await asyncio.gather(client(col), server(queue, col))
    print("---------------------------------------------------------------"
          "-------------------------------------------")
    print("Все запросы обработаны")


asyncio.run(main())
