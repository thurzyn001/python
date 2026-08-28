try:
    num = int(input('Digite um número inteiro: '))
    base = int(input('''E qual será a base de conversão?
1 = binário
2 = octal
3 = hexadecimal
'''))
    if base == 1:
        print('a base de conversão escolhida foi binário.')
        import time

        print("Carregando", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\nCarregamento concluído")

        print(f'O número {num} convertido para base binária é: {bin(num)[2:]}')
    elif base == 2:
        print('a base de conversão escolhida foi octal.')
        import time

        print("Carregando", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\nCarregamento concluído")

        print(f'O número {num} convertido para base octal é: {oct(num)[2:]}')
    elif base == 3:
        print('a base de conversão escolhida foi hexadecimal.')
        import time

        print("Carregando", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\nCarregamento concluído")

        print(f'O número {num} convertido para base hexadecimal é: {hex(num)[2:]}')
    else:
        print('Entrada inválida. Digite apenas números entre 1 e 3.')
except ValueError:
    print('Entrada Inválida. Tente novamente')
