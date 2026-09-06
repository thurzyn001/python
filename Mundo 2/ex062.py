from subprocess import run
from os import name
import sys

def limpar_tela():
    run(['cmd', '/c', 'cls']) if name == 'nt' else run(['clear'])

def apagar_linhas(quantidade=1):
    for _ in range(quantidade):
        sys.stdout.write("\033[1A\033[K")
    sys.stdout.flush()

def pedir_inteiro(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem))

            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                input("Pressione Enter para tentar novamente...")
                apagar_linhas(3)
                continue

            return valor

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
            input("Pressione Enter para tentar novamente...")
            apagar_linhas(3)

def mostrar_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def definir_pa(inicio=None, quantidade=None, razao=None):
    if inicio is None:
        inicio = pedir_inteiro("Digite o termo inicial da PA: ")
        print()
    if quantidade is None:
        quantidade = pedir_inteiro("Digite a quantidade de termos da PA: ", 1)
        print()
    if razao is None:
        razao = pedir_inteiro("Digite a razão da PA: ")
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

def exibir_pa(pa, soma, inicio, quantidade, razao):
    limpar_tela()
    mostrar_cabecalho("   PA Gerada:   ")
    
    if pa:
        print(f"Parâmetros atuais -> Início: {inicio} | Quantidade: {quantidade} | Razão: {razao}\n")
        print("Início da PA → ", end="")
        print(" → ".join(map(str, pa)) + " → Fim da PA.")
        print(f"\nSoma dos termos da PA: {soma}\n")

def menu_alterar_parametro(inicio, quantidade, razao):
    while True:
        limpar_tela()
        mostrar_cabecalho("   Alterar Parâmetro   ")
        print(f"[1] Alterar termo inicial (Atual: {inicio})")
        print(f"[2] Alterar quantidade de termos (Atual: {quantidade})")
        print(f"[3] Alterar razão (Atual: {razao})")
        print("[4] Voltar\n")

        opcao = input("O que deseja fazer? ").strip()
        print()

        if opcao == "1":
            inicio = pedir_inteiro("Novo termo inicial: ")

        elif opcao == "2":
            quantidade = pedir_inteiro("Nova quantidade de termos: ", 1)

        elif opcao == "3":
            razao = pedir_inteiro("Nova razão: ")

        elif opcao == "4":
            return inicio, quantidade, razao

        else:
            print("\nOpção inválida!")
            input("Pressione Enter para tentar novamente...")

def menu_opcoes(inicio, quantidade, razao):
    mostrar_cabecalho("   Menu da PA   ")
    print(" [1] Recomeçar")
    print(" [2] Alterar parâmetros")
    print(" [3] Sair\n")
    
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        limpar_tela()
        mostrar_cabecalho("   Nova PA   ")
        return definir_pa()  

    elif opcao == "2":
        return menu_alterar_parametro(inicio, quantidade, razao)

    elif opcao == "3":
        limpar_tela()
        print("Programa encerrado. Até logo!")
        sys.exit()

    else:
        print("\nOpção inválida!")
        input("Pressione Enter para tentar novamente...")
        return inicio, quantidade, razao

def main():
    limpar_tela()
    mostrar_cabecalho("   Progressão Aritmética v.3.0   ")
    
    inicio, quantidade, razao = definir_pa()

    while True:
        resultado, soma = calcular_pa(inicio, quantidade, razao)
        exibir_pa(resultado, soma, inicio, quantidade, razao)
        
        inicio, quantidade, razao = menu_opcoes(inicio, quantidade, razao)

if __name__ == "__main__":
    main()
