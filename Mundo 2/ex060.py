from subprocess import run
from os import name

def limpar_tela():
    run(['cls' if name == 'nt' else 'clear'], shell=True)

def mostra_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
    
def main():
    limpar_tela()
    mostra_cabecalho("   Fatorial v.1.0  ")
    num = int(input("Digite um número para calcular seu fatorial: "))
    print()
    resultado = fatorial(num)
    decrescente = list(range(num, 0, -1))
    expressao = " x ".join(map(str, decrescente))
    print(f"Calculando: {num}! = {expressao} = {resultado}")

main()
