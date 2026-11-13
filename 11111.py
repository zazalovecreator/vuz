import asyncio

async def f():
    await asyncio.sleep(0.5)
    return "готово"

async def main():
    t = asyncio.create_task(f())    # запущена в фоне
    print("делаю другое дело")      # идёт, пока f ждёт
    x = await t                     # забираем результат
    print(x)

asyncio.run(main())