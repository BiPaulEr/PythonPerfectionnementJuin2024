import asyncio
import time 
import random

class ContextManagerCustom:
    async def __aenter__(self):
        print("Entrée dans le contexte, ca prend du temps")
        await asyncio.sleep(3)
        return "ressource"
    async def __aexit__(self, exc_type, exc, traceback):
        print("Fermeture du contexte")

async def worker():
    timestosleep = random.randint(1, 5)
    print(f"Worker needs {timestosleep} to finish.")
    await asyncio.sleep(timestosleep)

async def creation_de_toutes_les_taches():
    async with ContextManagerCustom() as ressource:
        print(ressource)
        for i in range(0, 5):
            task = asyncio.create_task(worker())
        await task
        
 
asyncio.run(creation_de_toutes_les_taches())
