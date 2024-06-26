import asyncio
import time 
import random

async def factoriel(n):
    await asyncio.sleep(0.1)
    if n <= 1:
        return 1
    else:
        result = await factoriel(n-1)
        return n * result

async def creation_de_toutes_les_taches():
    donnee = [5, 7, 3, 6]
    tasks = [asyncio.create_task(factoriel(num)) for num in donnee]
    for task in asyncio.as_completed(tasks):
        result = await task
        print(f"Result received : {result}")
 
asyncio.run(creation_de_toutes_les_taches())
