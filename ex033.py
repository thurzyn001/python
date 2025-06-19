try:
    num1 = float(input('\033[38;2;100;149;237mDigite o primeiro número: \033[m'))
    num2 = float(input('\033[38;2;100;149;237mDigite o segundo número: \033[m'))
    num3 = float(input('\033[38;2;100;149;237mDigite o terceiro número: \033[m'))

    numeros = [num1, num2, num3]
    numeros.sort()

    print(f'''
\033[38;2;0;128;0mO menor número é {numeros[0]}
O número do meio é {numeros[1]}
O maior número é {numeros[2]}\033[m''')

except ValueError:
    print('\033[38;2;255;0;0mEntrada Inválida! Por favor digite apenas números.\033[m')
