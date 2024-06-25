import requests

class HTTPSession:
    def __enter__(self):
        self.session = requests.Session()
        return self.session
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()

with HTTPSession() as session:
    header = {'Accept': 'text/plain'}
    url = "https://icanhazdadjoke.com/"
    response = session.get(url, headers = header)
    if (response.status_code != 200):
        print(" ERROR in the response")
    else:
        print(response.text)

from contextlib import contextmanager
import requests
 
@contextmanager
def contexte_blague():
    print("debut")
    session = requests.Session()
    try:
        yield session
    finally:
        session.close()
# appel
with contexte_blague() as session:
    print("ouvrir une session http sur l'url icanhazdadjoke.com")
    session.headers.update({'Accept': 'text/plain'})
    blague = session.get("http://icanhazdadjoke.com")
    if blague.status_code == 200:
            print(f"la blague est : {blague.text}")
    else:
        print("Erreur ...")

