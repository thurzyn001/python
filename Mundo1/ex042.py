from sys import exit

try:
    ladoA = float(input('Digite o comprimento do lado A: '))
    if ladoA <=0:
        print('Os valores não podem ser menores ou iguais a zero.')
        exit()
    ladoB = float(input('Digite o comprimento do lado B: '))
    if ladoB <=0:
        print('Os valores não podem ser menores ou iguais a zero.')
        exit()
    ladoC = float(input('Digite o comprimento do lado C: '))
    if ladoC <=0:
        print('Os valores não podem ser menores ou iguais a zero.')
        exit()
    if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
        print(f'''
Os segmentos de reta A, B e C com valores {ladoA}, {ladoB} e {ladoC}
podem formar um triângulo.
    ''')
        if ladoA == ladoB == ladoC:
            print('O triângulo ABC é Equilátero pois possui todos os lados iguais.')
        elif ladoA == ladoB != ladoC or ladoA == ladoC != ladoB or ladoB == ladoC != ladoA:
            print('O triângulo ABC é Isóceles pois possui apenas dois lados iguais.')
        elif ladoA != ladoB != ladoC:
            print('O triângulo ABC é Escaleno pois todos os lados são diferentes.')
    else:
        print(f'''
Os segmentos de reta A, B e C com valores {ladoA}, {ladoB} e {ladoC}
não podem formar um triângulo.''')
except ValueError:
    print('Entrada inválida tente novamente.')
