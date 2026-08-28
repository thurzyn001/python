from random import randint
from time import sleep

try:
    num = randint(0, 5)
    resposta = int(input('''\033[38;2;100;150;255m
    Um número entre 0 e 5 aleatório foi escolhido.
    Tente adivinhar qual foi esse número: \033[m'''))
    print('\033[38;2;255;255;100mPROCESSANDO...\033[m')
    sleep(1)
    if resposta < 0 or resposta > 5:
        print('''\033[38;2;255;0;0m
    Cê é burro? falei entre 0 e 5 animal!\033[m''')
    elif resposta == num:
        print(f'''\033[38;2;0;255;0m
    Acertô mizeravi, era {num} memo. Parabéns!\033[m''')
    else:
        print(f'''\033[38;2;255;100;0m
    Errroo, errou feio, errou rude, era {num}, Mt burrowkkk!\033[m''')
except ValueError:
    print('\033[38;2;255;0;0mEntrada inválida, tente novamente utilizando apenas números inteiros!\033[m')
