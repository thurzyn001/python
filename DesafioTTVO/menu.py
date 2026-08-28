import os
import time
import panela

def Menu():
    os.system("cls")
    opcao = 0
    while opcao != 2:
        print("==== Panela do TTVO ====")
        print("1.Escolher receita")
        print("3.Sair")
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                print("Wip")
                time.sleep(0.5)
                os.system("cls")
            case 2:
                print("Wip")
            case 3:
                print("Saindo...")
                exit()
Menu()
