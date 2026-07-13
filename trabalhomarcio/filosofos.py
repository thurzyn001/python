import threading
import time

garfos = [threading.Lock() for i in range(5)]

def filosofo(i):
    while True:
        print(f"Filósofo {i} está esperando\n")
        time.sleep(1)

        esquerda = garfos[i]
        direita = garfos[(i + 1) % 5]

        with esquerda:
            with direita:
                print(f"Filósofo {i} está comendo\n")
                time.sleep(1)

threads = []

for i in range(5):
    t = threading.Thread(target=filosofo, args=(i,))
    threads.append(t)
    t.start()