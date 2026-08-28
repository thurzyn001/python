import os
import subprocess

subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True)

print("Programa para classificar triângulos com base nos lados fornecidos pelo usuário.\n")

l1 = int(input("Digite o valor do lado 1: "))
l2 = int(input("Digite o valor do lado 2: "))
l3 = int(input("Digite o valor do lado 3: "))

def classifica_triangulo(l1, l2, l3):
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return "\nOs lados do triângulo devem ser maiores que zero."
    else:
        if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
            return "\nOs lados fornecidos não formam um triângulo válido."
        else:
            if l1 == l2 == l3:
                return "\nO triângulo é Equilátero"
            elif l1 == l2 or l1 == l3 or l2 == l3:
                return "\nO triângulo é Isósceles"
            else:
                return "\nO triângulo é Escaleno"

print(classifica_triangulo(l1, l2, l3))
