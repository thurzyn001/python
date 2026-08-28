import os
import subprocess

subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True)

print("Gerenciador de Pagamentos:\n")

preco = float(input("Digite o preço do produto: ")) 

print("\nEscolha a forma de pagamento:\n")
print("1 - À vista (dinheiro ou cheque) - 10% de desconto")
print("2 - À vista no cartão - 5% de desconto")
print("3 - Em até 2x no cartão - Preço normal")
print("4 - 3x ou mais no cartão - 20% de juros")

opcao = int(input("\nDigite a opção desejada (1, 2, 3 ou 4): "))

def calcular_pagamento(preco, opcao):
    if preco <= 0:
        return "\nO preço do produto deve ser maior que zero."
    else:
        if opcao == 1:
            desconto = preco * 0.10
            preco_final = preco - desconto
            return f"\nO preço final com desconto de 10% é: R$ {preco_final:.2f}"
        elif opcao == 2:
            desconto = preco * 0.05
            preco_final = preco - desconto
            return f"\nO preço final com desconto de 5% é: R$ {preco_final:.2f}"
        elif opcao == 3:
            return f"\nO preço total é: R$ {preco:.2f} (sem desconto) que será dividido em 2 parcelas de R$ {preco / 2:.2f} cada."
        elif opcao == 4:
            parcelas = int(input("\nDigite o número de parcelas (3 ou mais): "))
            if parcelas < 3:
                return "\nNúmero de parcelas inválido. Para esta opção, o número de parcelas deve ser 3 ou mais."
            juros = preco * 0.20
            preco_final = preco + juros
            return f"\nO preço total com juros de 20% é: R$ {preco_final:.2f} que será dividido em {parcelas} parcelas de R$ {preco_final / parcelas:.2f} cada."
        else:
            return "\nOpção inválida. Por favor, escolha uma opção entre 1 e 4."
        
print(calcular_pagamento(preco, opcao))
