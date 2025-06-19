from sys import exit

try:
    idade = int(input('Digite sua idade: '))
    if idade <= 0:
        print('''
Entrada Inválida.
Encerrando programa.
            ''')
        exit()
    elif idade == 1:
        print('Por ter 1 ano, você disputará a categoria MIRIM.')
    elif idade <= 9:
        print(f'Por ter {idade} anos, você disputará a categoria MIRIM.')
    elif idade > 9 or idade <= 14:
        print(f'Por ter {idade} anos, você disputará a categoria INFANTIL.')
    elif idade > 14 or idade <= 19:
        print(f'Por ter {idade} anos, você disputará a categoria JUNIOR.')
    elif idade == 20:
        print('Por ter 20 anos, você disputará a categoria SÊNIOR.')
    else:
        print(f'por ter {idade} anos, você disputará a categoria MASTER.')
except ValueError:
    print('Digite apenas NÚMEROS INTEIROS.')
