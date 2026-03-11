import threading
import time

garfos = [threading.Lock() for _ in range(5)]

def filosofo(i):
    while True:
        print(f"Filósofo {i} está pensando")
        time.sleep(1)

        print(f"Filósofo {i} quer comer")

        garfo_esq = garfos[i]
        garfo_dir = garfos[(i+1)%5]

        with garfo_esq:
            with garfo_dir:
                print(f"Filósofo {i} está comendo")
                time.sleep(1)

for i in range(5):
    threading.Thread(target=filosofo, args=(i,)).start()