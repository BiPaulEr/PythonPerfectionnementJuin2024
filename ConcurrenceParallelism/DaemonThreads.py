from threading import Thread
import threading
import time
class CustomThread(Thread):
    def __init__(self, caractere = "", name = None, daemon = None, target = None):
        super().__init__(name = name, daemon = daemon, target = target)
        self.name = name
        self.caractere = caractere
        
    def run(self):
        print(self.name, flush=True)
        for i in range(0, 10):
            for j in range(0, 10):
                print(self.caractere, end="", flush=False)
            

thread_asterix = CustomThread("*", name = "Asterix", daemon = True)
thread_point = CustomThread(".", name = "Point", daemon = False)
time.sleep(1)
thread_asterix.start()
thread_point.start()
time.sleep(3)
print(threading.active_count())
print(threading.current_thread())
print(threading.enumerate())
    