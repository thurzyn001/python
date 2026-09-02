from subprocess import run
from random import randint

def limpar_tela():
    run(["cls"], shell=True)

def limpar_linha():
    print("\033[F\033[K", end="")

def mostra_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def Escolha_Pc():
    return randint(0, 10)

def Escolha_Jogador():
    while True:
        try:
            escolha = int(input("Escolha um número entre 0 e 10: "))
            if 0 <= escolha <= 10:
                return escolha
            else:
                print("Número inválido. Digite um número entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def jogo(escolha_pc, escolha_jogador):
    cont = 1
    while escolha_pc != escolha_jogador:
        limpar_linha()
        print(f"{cont}ª tentativa: {escolha_jogador}")
        cont += 1
        if escolha_jogador < escolha_pc:
            print("\nMaior... Tente novamente.\n")
        else:
            print("\nMenor... Tente novamente.\n")
        escolha_jogador = Escolha_Jogador()
    limpar_tela()
    mostra_cabecalho("   Adivinhação v.2.0.   ")
    print(f"Parabéns! Você acertou o número {escolha_pc} em {cont} tentativas.")

def main():
    limpar_tela()
    mostra_cabecalho("   Adivinhação v.2.0.   ")
    pc = Escolha_Pc()
    jogador = Escolha_Jogador()
    jogo(pc, jogador)

main()
