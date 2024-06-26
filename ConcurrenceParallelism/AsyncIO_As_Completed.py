import asyncio
import time 
import random

async def worker(label):
    timestosleep = random.randint(1, 10)
    print(f"Worker {label} needs {timestosleep} to finish.")
    await asyncio.sleep(timestosleep)  # Simulez un délai de réseau
    result = random.randint(0, 100)  # Générez une température aléatoire
    print(f"Worker {label} has ended")
    return f"Worker {label} result is {result}"

async def creation_de_toutes_les_taches():
    tasks = [asyncio.create_task(worker(label)) for  label in ["A", "B", "C", "D"]]
    for task in asyncio.as_completed(tasks):
        result = await task
        print(f"Result received : {result}")

    
asyncio.run(creation_de_toutes_les_taches())
