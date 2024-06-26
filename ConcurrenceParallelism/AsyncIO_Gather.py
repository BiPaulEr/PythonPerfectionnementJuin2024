import asyncio
import time 
import random

async def read_file(file_name):
    await asyncio.sleep(random.randint(1, 5))  # Simulate the delay of reading a file
    print(f"{file_name} read successfully")
    return(f"Contents of {file_name}")

def log_task(task):
    print(f"{task.result()}")

async def creation_de_toutes_les_taches():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = []
    for file in files:
        task = asyncio.create_task(read_file(file))
        task.add_done_callback(log_task)
        tasks.append(task)
    listdereponse = await asyncio.gather(*tasks)
    print("Resultat après gather")
    print(listdereponse)
    
asyncio.run(creation_de_toutes_les_taches())
