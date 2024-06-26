import asyncio
import time 
import random
async def worker(identifiant):
    sleep_time_in_secs = random.randint(0, 10)
    print(f"Je suis {identifiant} je vais sleep pendant {sleep_time_in_secs} ")
    await asyncio.sleep(sleep_time_in_secs)
    print(f"Je finis de sleep pendant {sleep_time_in_secs} ")

async def list_detache_a_faire():
    for i in range(0, 3):
        await worker(str(i))
    

asyncio.run(list_detache_a_faire())
time.sleep(10)