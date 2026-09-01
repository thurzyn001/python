from subprocess import run
from datetime import date

def limpar_tela():
    run(["cls"], shell=True)

def mostra_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def defini_loop():
    num = int(input("Número de datas de nascimento que serão digitadas: "))
    return num

def verifica_maioridade(ano):
    ano_atual = date.today().year
    if ano <= ano_atual - 18:
        return True
    else:
        return False

def main():
    num = defini_loop()
    print("")
    maior = 0
    menor = 0

    for i in range(num):
        ano = int(input(f"Digite o ano de nascimento da {i + 1}ª pessoa: "))
        print("")
        if verifica_maioridade(ano):
            maior += 1
        else:
            menor += 1

    print(f"Ao todo tivemos {maior} pessoas maiores de idade e {menor} pessoas menores de idade.")

def start():
    limpar_tela()
    mostra_cabecalho("É de maior?? v.2.0")
    main()

start()
