import os
import subprocess
from time import sleep

def limpar_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True, check=False,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def mostrar_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def ler_inteiro(mensagem):
    """Lê um número inteiro do usuário com validação."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.\n")

def obter_novos_numeros():
    """Solicita dois números inteiros ao usuário."""
    print("Informe os novos números:")
    num1 = ler_inteiro("Primeiro número: ")
    num2 = ler_inteiro("Segundo número: ")
    return num1, num2

def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def maior(a, b):
    return a if a > b else b

def exibir_resultado(operacao, a, b, resultado):
    print(f"\n{operacao} de {a} e {b} é: {resultado}\n")
    input("Pressione Enter para continuar...")

def main():
    limpar_tela()
    mostrar_cabecalho("   Exercício 059 - Menu de Opções   ")
    num1, num2 = obter_novos_numeros()

    while True:
        limpar_tela()
        mostrar_cabecalho("Menu de Opções")
        print(f"Números atuais: {num1} e {num2}\n")
        print("1 - Somar")
        print("2 - Multiplicar")
        print("3 - Ver maior")
        print("4 - Novos números")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            resultado = somar(num1, num2)
            exibir_resultado("A soma", num1, num2, resultado)
        elif opcao == "2":
            resultado = multiplicar(num1, num2)
            exibir_resultado("O produto", num1, num2, resultado)
        elif opcao == "3":
            resultado = maior(num1, num2)
            exibir_resultado("O maior número", num1, num2, resultado)
        elif opcao == "4":
            num1, num2 = obter_novos_numeros()
        elif opcao == "5":
            limpar_tela()
            print("Saindo do programa...")
            sleep(1)
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")
            sleep(1)

if __name__ == "__main__":
    main()
