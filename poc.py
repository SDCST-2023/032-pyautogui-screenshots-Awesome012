#!python3

import asyncio
import time

async def t1():
    for i in range(3):
        print("task1")
        for j in range(10):
            time.sleep(0.25)
            print('blocking')
        await asyncio.sleep(1)

async def t2():
    while True:
        print("task 2")
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task( t1() )
    task2 = asyncio.create_task( t2() )
    await task1
    await task2


asyncio.run( main() )