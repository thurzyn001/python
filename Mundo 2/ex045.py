import os
import subprocess
import random

subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True)

print("Jogo de Pedra, Papel e Tesoura:\n")

def jogar_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    
    if jogador not in opcoes:
        return "\nOpção inválida! Por favor, escolha pedra, papel ou tesoura."

    computador = random.choice(opcoes)
    
    print(f"\nVocê escolheu: {jogador}\n")
    print(f"O computador escolheu: {computador}")
    
    if jogador == computador:
        return "\nEmpate!"
    elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
        return "\nVocê venceu!"
    else:
        return "\nO computador venceu!"

print(jogar_pedra_papel_tesoura())
