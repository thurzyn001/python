import os
import subprocess

subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True)

print("Programa para seleção de categorial da confederação nacional de natação:\n")

idade = int(input("Digite a idade do atleta: "))

def categoria_atleta(idade):

    if idade <= 0:
        return "\nIdade inválida! Digite uma idade maior que 0."
    else:
        if idade <= 9:
            return "\nO atleta pertence à categoria MIRIM."
        elif idade <= 14:
            return "\nO atleta pertence à categoria INFANTIL."
        elif idade <= 19:
            return "\nO atleta pertence à categoria JÚNIOR."
        elif idade <= 25:
            return "\nO atleta pertence à categoria SÊNIOR."
        else:
            return "\nO atleta pertence à categoria MASTER."

print(categoria_atleta(idade))
