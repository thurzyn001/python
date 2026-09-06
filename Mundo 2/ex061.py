from subprocess import run
from os import name

def limpar_tela():
    run(['cmd', '/c', 'cls']) if name == 'nt' else run(['clear'])

def mostrar_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def definir_pa():
    inicio = int(input("Digite o termo inicial da PA: "))
    print()
    quantidade = int(input("Digite a quantidade de termos da PA: "))
    print()
    razao = int(input("Digite a razão da PA: "))
    print()

    return inicio, quantidade, razao

def calcular_pa(inicio, quantidade, razao):
    soma = 0
    cont = 0
    pa = []
    while cont < quantidade:
        termo = inicio + cont * razao
        pa.append(termo)
        cont += 1
        soma += termo
    return pa, soma

def exibir_pa(pa, soma):
    mostrar_cabecalho("   PA Gerada:   ")
    print("Início da PA → ", end="")
    print(" → ".join(map(str, pa)) + " → Fim da PA.")
    print(f"\nSoma dos termos da PA: {soma}")

def pa():
    inicio, quantidade, razao = definir_pa()
    resultado, soma = calcular_pa(inicio, quantidade, razao)
    exibir_pa(resultado, soma)

def main():
    limpar_tela()
    mostrar_cabecalho("   Progressão Aritimética v.2.0   ")
    pa()

if __name__ == "__main__":
    main()
