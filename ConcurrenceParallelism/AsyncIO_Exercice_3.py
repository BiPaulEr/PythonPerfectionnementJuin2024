import asyncio
import time 
import random

async def worker(label, duration):
    print(f"Worker {label} needs {duration} to finish.")
    await asyncio.sleep(duration)  # Simulez un délai de réseau
    result = random.randint(0, 100)  # Générez une température aléatoire
    if (result < 50):
        raise ValueError("PAS DE CHANCE")
    print(f"Worker {label} has ended")
    return f"Worker {label} result is {result}"

async def creation_de_toutes_les_taches():
    duration = [3, 1, 4, 2]
    tasks = (asyncio.create_task(worker(label, duree)) for label, duree in zip(["A", "B", "C", "D"], duration))
    compteur = 0
    for task in asyncio.as_completed(tasks):
        try : 
            result = await task
            compteur += 1
            print(f"Nombre de tache complete : {compteur}")
            print(f"Result received : {result}")
        except ValueError as e:
            print(f"Tache echoue : {e}")

asyncio.run(creation_de_toutes_les_taches())
