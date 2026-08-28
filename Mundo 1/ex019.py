from random import choice

a1 = str(input('\033[38;2;173;216;230mDigite o nome do primeiro aluno:\033[m '))
a2 = str(input('\033[38;2;173;216;230mDigite o nome do segundo aluno:\033[m '))
a3 = str(input('\033[38;2;173;216;230mDigite o nome do terceiro aluno:\033[m '))
a4 = str(input('\033[38;2;173;216;230mDigite o nome do quarto aluno:\033[m '))

lista = [a1, a2, a3, a4]
print(f'\033[38;2;173;216;230mO aluno(a) escolhido foi o(a): {choice(lista)}\033[m')
