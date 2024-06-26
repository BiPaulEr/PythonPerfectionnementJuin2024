import asyncio
import time 
import random

def print_the_result(task):
    print("On est dans le callback the result est  ", task.result())

def info(task):
    print("task cancelled ? ", task.cancelled())
    print("task done ? ", task.done())
    try :
        print("task.exeception() ", task.exception())
    except asyncio.exceptions.InvalidStateError as invalidate:
        print(f"Exception par .exception() : {invalidate}")
    try :
        print("result ", task.result())
    except asyncio.exceptions.InvalidStateError as invalidate:
        print(f"Exception par .result() : {invalidate}")

async def worker(identifiant):
    sleep_time_in_secs = random.randint(0, 10)
    print(f"Je suis {identifiant} je vais sleep pendant {sleep_time_in_secs} ")
    await asyncio.sleep(sleep_time_in_secs)
    print(f"Je finis de sleep pendant {sleep_time_in_secs} ")
    return str(f"Worker {identifiant}: is done ")

async def list_detache_a_faire():
    tasks = []
    for i in range(0, 3):
        task =  asyncio.create_task(worker(str(i))) 
        task.add_done_callback(print_the_result)
    await task
    
    

asyncio.run(list_detache_a_faire())
time.sleep(10)