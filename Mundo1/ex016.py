'''from math import trunc
num = float(input('Digite um número real qualquer:'))
print (f' A parte inteira de {num} é {trunc(num)}.')'''

num = float(input('\033[38;2;255;105;180mDigite um número real qualquer:\033[m '))
print(f'\033[38;2;255;105;180mO número digitado foi {num} e sua parte inteira é {int(num)}.\033[m')

