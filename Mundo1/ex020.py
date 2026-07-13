from random import shuffle

a1 = str(input('\033[38;2;173;216;230mPrimeiro aluno:\033[m '))
a2 = str(input('\033[38;2;173;216;230mSegundo aluno:\033[m '))
a3 = str(input('\033[38;2;173;216;230mTerceiro aluno:\033[m '))
a4 = str(input('\033[38;2;173;216;230mQuarto aluno:\033[m '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'\033[38;2;173;216;230mOrdem de apresentação: {lista}\033[m')
