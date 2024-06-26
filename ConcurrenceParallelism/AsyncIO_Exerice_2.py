import asyncio
import time 
import random

async def fetch_weather(city):
    await asyncio.sleep(1)  # Simulez un délai de réseau
    temperature = random.randint(15, 25)  # Générez une température aléatoire
    print(f"Température pour {city} : {temperature}°C")
    return {"ville": city, "température": temperature}

async def creation_de_toutes_les_taches():
    cities = ["City1","City2","City3"]
    #create_task not required for gather
    #listdereponse = await asyncio.gather(*(asyncio.create_task(fetch_weather(city)) for city in cities)) 
    listdereponse = await asyncio.gather(*(fetch_weather(city) for city in cities))
    moyenne = sum([rapport_city["température"] for rapport_city in listdereponse]) / len(listdereponse)
    
    print("Resultat après gather")
    print(listdereponse)
    print("Resultat après moyenne")
    print(moyenne)
    
asyncio.run(creation_de_toutes_les_taches())
