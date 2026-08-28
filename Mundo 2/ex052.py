from subprocess import run

def limpar_tela():
    run(["cls"], shell= True)

def cabecalho(msg):
    linha = "=" * len(msg)
    print(linha)
    print(msg)
    print(linha)
    print("")

def verifica_primo(num):
    cont = 0
    divisores = set()

    for i in range(1, num + 1):
        if num % i == 0:
            cont += 1
            divisores.add(i)

    return cont, divisores
    
def start():
    limpar_tela()
    cabecalho("É Primo?? v.1.0")

    num = int(input("Digite um número: "))
    print("")

    cont, divisores = verifica_primo(num)

    for i in range(1, num + 1):
        if i in divisores:
            print(f"\033[31m{i}\033[m", end=" ")
        else:
            print(f"\033[33m{i}\033[m", end=" ")

    print("")

    if cont == 2:
        print(f"\nO número {num}, foi divisível apenas 2 vezes, logo ele É UM NÚMERO PRIMO!")
    else:
        print(f"\nO número {num}, foi divisível {cont} vezes, logo ele NÃO É UM NÚMERO PRIMO!")

start()
