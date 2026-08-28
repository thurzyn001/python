from os import name
from subprocess import run

def limpar_tela():
    run(["cls"] if name == "nt" else ["clear"], shell=True)

def calcular(inicio, fim):
    soma = 0
    cont = 0

    for i in range(inicio, fim + 1):
        if i % 2 != 0 and i % 3 == 0:
            soma += i
            cont += 1

    return soma, cont

def start():
    limpar_tela()

    print("Soma de números ímpares múltiplos de 3 em um Intervalo:\n")

    inicio = int(input("Digite o início do intervalo: "))
    print("")
    fim = int(input("Digite o fim do intervalo: "))

    soma, cont = calcular(inicio, fim)

    print(f"\nExistem {cont} números ímpares múltiplos de 3 entre {inicio} e {fim} e a soma deles é {soma}.")

start()
