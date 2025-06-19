numero = int(input('\033[38;2;255;105;180mDigite um número entre 1 e 9999: \033[m'))
print(f'\033[38;2;255;105;180mAnalisando o número {numero}.\033[m')
if 1 <= numero <= 9999:
    listadigitos = [int(digito) for digito in str(numero).zfill(4)]
    print(
        f'''
\033[38;2;0;206;209munidade: {listadigitos[3]}\033[m
\033[38;2;0;206;209mdezena: {listadigitos[2]}\033[m
\033[38;2;0;206;209mcentena: {listadigitos[1]}\033[m
\033[38;2;0;206;209mmilhar: {listadigitos[0]}\033[m'''
    )
else:
    print('\033[38;2;255;0;0mNúmero fora do intervalo. Tente novamente.\033[m')


#Código do Guanabara:
# num = (int(input('Informe um número entre 1 e 9999: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print(f'''
# Analisando o número {num}
# unidade: {u}
# dezena: {d}
# centena: {c}
# milhar: {m}''')
