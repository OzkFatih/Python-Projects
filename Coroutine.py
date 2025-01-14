import time
import asyncio

def f1():
    print("F1: Start")
    time.sleep(5)
    print("F1: End")

def f2():
    print("F2: Start")
    time.sleep(2)
    print("F2: End")

def sync_main():
    time_start = time.time()
    print("Sync Main: Start")
    f1()
    f2()
    print("Sync Main: End")
    time_end = time.time()
    print(f"Time taken: {time_end - time_start}")

async def af1():
    print("AF1: Start")
    await asyncio.sleep(5)
    print("AF1: End")

async def af2():
    print("AF2: Start")
    await asyncio.sleep(2)
    print("AF2: End")

async def async_main():
    time_start = time.time()
    print("Async Main: Start")
    await asyncio.gather(af1(), af2())
    print("Async Main: End")
    time_end = time.time()
    print(f"Time taken: {time_end - time_start}")

if __name__ == "__main__":
    #sync_main()
    asyncio.run(async_main())