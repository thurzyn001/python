import os
import subprocess

subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True)

print("Calculadora de Imc:\n")

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        return "\nPeso e altura devem ser maiores que zero."
    else:
        imc = peso / (altura ** 2)
        if imc < 18.5:
            return f"\nSeu IMC é {imc:.2f}. Você está abaixo do peso."
        elif 18.5 <= imc < 24.9:
            return f"\nSeu IMC é {imc:.2f}. Você está com o peso ideal."
        elif 25 <= imc < 29.9:
            return f"\nSeu IMC é {imc:.2f}. Você está com sobrepeso."
        elif 30 <= imc <= 40:
            return f"\nSeu IMC é {imc:.2f}. Você está com obesidade."
        else:
            return f"\nSeu IMC é {imc:.2f}. Você está com obesidade mórbida."

print(calcular_imc(peso, altura))
