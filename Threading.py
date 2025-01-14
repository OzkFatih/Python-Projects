import threading
import time

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

sync_main()