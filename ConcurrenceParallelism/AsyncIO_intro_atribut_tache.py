import asyncio
import time 
import random

def info(task):
    print("task cancelled ? ", task.cancelled())
    print("task done ? ", task.done())
    try :
        print("task.exeception() ", task.exception())
    except asyncio.exceptions.InvalidStateError as invalidate:
        print(f"{invalidate}")
    #print("result ", task.result())

async def worker(identifiant):
    sleep_time_in_secs = random.randint(0, 10)
    print(f"Je suis {identifiant} je vais sleep pendant {sleep_time_in_secs} ")
    await asyncio.sleep(sleep_time_in_secs)
    print(f"Je finis de sleep pendant {sleep_time_in_secs} ")

async def list_detache_a_faire():
    for i in range(0, 3):
        task =  asyncio.create_task(worker(str(i)))
        info(task)
    await task
    

asyncio.run(list_detache_a_faire())
time.sleep(10)