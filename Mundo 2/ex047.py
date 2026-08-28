from os import name
from subprocess import run
from time import sleep

def limpar_tela():
    run(["cls"] if name == "nt" else ["clear"], shell=True)

def contar_pares(inicio, fim):
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            print(i, end=" ", flush=True)
            sleep(0.5)

def start():
    limpar_tela()

    print("Contagem de Números Pares em um Intervalo:\n")

    inicio = int(input("Digite o início do intervalo: "))
    print("")
    fim = int(input("Digite o fim do intervalo: "))

    print(f"\nNúmeros pares entre {inicio} e {fim}:\n")
    contar_pares(inicio, fim)

    print("\n\nFim da contagem.")

start()
