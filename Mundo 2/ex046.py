from os import name
from subprocess import run
from time import sleep

def apagar_linhas(qtd):
    for _ in range(qtd):
        print("\033[1A\033[2K", end="")

def contagem_regressiva():
    for i in range(10, -1, -1):
        print(i, "\n")
        sleep(1)
        apagar_linhas(2)
        
    print("Feliz Ano Novo!")

run(["cls"] if name == "nt" else ["clear"], shell=True)

print("Contagem Regressiva para os Fogos de Artifício:\n")

contagem_regressiva()
