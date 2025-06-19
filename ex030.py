try:
    num = int(input('\033[38;2;255;165;0mDigite um número inteiro qualquer: \033[m'))
    resultado = f'\033[38;2;34;139;34m{num} é par.\033[m' if num % 2 == 0 else f'\033[38;2;255;0;0m{num} é ímpar.\033[m'
    print(resultado)
except ValueError:
    print('''\033[38;2;255;0;0m
Eu não falei UM NÚMERO INTEIRO QUALQUER? PQ VC DIGITOU OUTRA COISA?
Você é burro ou se faz? Porque não é possível!\033[m''')
