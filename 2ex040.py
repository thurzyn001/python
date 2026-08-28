import os
import time
import subprocess

subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True)

barra = "=" * 51

VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
RESET = "\033[0m"

def cabecalho():
    print(barra)
    print("     BEM VINDO AO PROGRAMA DE CÁLCULO DE MÉDIA")
    print(barra)

def apagar_linhas(qtd):
    for _ in range(qtd):
        print("\033[1A\033[2K", end="")

def voltar_linha():
    print("\033[1A", end="")

def ler_nota(numero,):

    nota = float(input(f"\nDigite a {numero}ª nota: "))

    while nota < 0 or nota > 10:
        print("\nNota inválida! Digite uma nota entre 0 e 10.\n")
        time.sleep(0.5)

        apagar_linhas(4)
        voltar_linha()

        nota = float(input(f"\nDigite a {numero}ª nota: "))

    return nota

def media(nota1, nota2):
    return (nota1 + nota2) / 2

def respostaFinal(mediaFinal):

    if mediaFinal < 5:
        print(f"{VERMELHO}\nPor possuir média {mediaFinal:.2f} e o mínimo exigido para recuperação é 5.0, você foi reprovado(a). Mais sorte na próxima!{RESET}")
    elif mediaFinal < 7:
        print(f"{AMARELO}\nPor possuir média {mediaFinal:.2f} e o mínimo exigido para recuperação é 5.0, você está de recuperação, estude mais!{RESET}")
    else:
        print(f"{VERDE}\nParabéns! Por possuir média {mediaFinal:.2f} e o mínimo exigido para aprovação é 7.0, você foi aprovado(a).{RESET}")

cabecalho()

nota1 = ler_nota(1)
nota2 = ler_nota(2)

mediaFinal = media(nota1, nota2)

print("\n" + barra)
print(f"A média entre as notas {nota1} e {nota2} é: {mediaFinal:.2f}")
print(barra)
respostaFinal(mediaFinal)
