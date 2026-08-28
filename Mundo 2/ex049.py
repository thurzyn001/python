from os import name
from subprocess import run

def limpar_tela():
    run(["cls"] if name == "nt" else ["clear"], shell=True)

def tabuada(numero, fim):
    for i in range(0, fim + 1):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado:2}")

def start():
    limpar_tela()

    print("Tabuada v.2.0\n")

    numero = int(input("Digite o número para calcular a tabuada: "))
    print("")
    fim = int(input("Digite até qual número deseja calcular a tabuada: "))

    print(f"\nTabuada do {numero} do 0 até o {fim}:\n")
    tabuada(numero, fim)

start()
