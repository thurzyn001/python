from subprocess import run

def limpar_tela():
    run(["cls"], shell=True)

def soma_pares(qtd):
    soma = 0
    cont = 0  

    for i in range(qtd):
        num = int(input(f"Digite o {i + 1}º número: "))
        print("")
        if num % 2 == 0:
            soma += num
            cont += 1

    return soma, cont

def start():

    limpar_tela()

    print("Soma de Pares v.1.0\n")

    qtd = int(input("Digite a quantidade de números que deseja somar. OBS: Apenas números pares serão considerados: "))
    print("")
    soma, cont = soma_pares(qtd)
    print(f"Dos {qtd} números digitados, {cont} são pares e o resultado da soma deles é {soma}.")

start()
