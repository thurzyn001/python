from subprocess import run
from time import sleep

def limpar_tela():
    run(["cls"], shell=True)

def limpar_linha():
    print("\033[F\033[K", end="")

def limpar_tela():
    run(["cls"], shell=True)

def mostra_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def mostra_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def loop_while():
    opcao = "x"
    while opcao not in ["m", "M", "f", "F"]:
        opcao = input("Digite o sexo da pessoa [M/F]: ").strip()
        if opcao not in ["m", "M", "f", "F"]:
            opcao = "x"
            print("Opção inválida. Digite apenas M ou F.")
            limpar_linha()
            sleep(0.5)
            limpar_linha()
        else:
            print("")
            if opcao in ["m", "M"]:
                print("Sexo Masculino selecionado.")
            else:
                print("Sexo Feminino selecionado.")
            
def main():
    limpar_tela()
    mostra_cabecalho("   Teste de While.   ")
    loop_while()

main()
