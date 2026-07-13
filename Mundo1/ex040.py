from sys import exit

try:
    nota1 = float(input('Digite a primeira nota: '))
    if nota1 < 0 or nota1 > 10:
        print('''
Apenas NÚMEROS entre 0,0 e 10,0.
Encerrando programa.
            ''')
        exit()
    nota2 = float(input('Digite a segunda nota: '))
    if nota2 < 0 or nota2 > 10:
        print('''
Apenas NÚMEROS entre 0,0 e 10,0.
Encerrando programa.
            ''')
        exit()
    media = (nota1 + nota2) / 2
    if media < 5:
        print(f'''
REPROVADO, pois sua média foi {media:.2f}
e o mínimo para a aprovação é 5,0.
            ''')
    elif 5 <= media <= 6.9:
        print(f'''
RECUPERÇÃO, pois sua média foi {media:.2f}
e médias entre 5,0 e 6,9 dão direito a recuperação.
            ''')
    else:
        print(f'''
APROVADO, pois sua média foi {media:.2f}
e médias maiores ou iguais a 7,0 são o suficiente para aprovação.
PARABÉNS!
            ''')
except ValueError:
    print('Apenas NÚMEROS entre 0,0 e 10,0')
