km = float(input('\033[38;2;255;215;0mQual a quilometragem rodada com o carro? :\033[m '))
pkm = float(input('\033[38;2;255;215;0mE qual o valor cobrado por km rodado? R$:\033[m '))
dia = int(input('\033[38;2;255;215;0mQuantos dias ficou com o carro? :\033[m '))
pdia = float(input('\033[38;2;255;215;0mE qual o valor cobrado por dia? R$:\033[m '))

print(f'''
\033[38;2;0;255;127mKms rodados: {km} kms.\033[m
\033[38;2;0;255;127mPreço por km rodado: R${pkm:.2f} reais.\033[m
\033[38;2;0;255;127mTotalizando R${km * pkm:.2f} reais em relação à quilometragem rodada.\n\033[m
\033[38;2;0;191;255mNúmero de dias do aluguel: {dia}.\033[m
\033[38;2;0;191;255mPreço por dia alugado: R${pdia:.2f}.\033[m
\033[38;2;0;191;255mTotalizando: R${dia * pdia:.2f} reais em relação ao número de dias do aluguel.\n\033[m
\033[38;2;255;0;0mO valor total do aluguel é de: R${km * pkm + dia * pdia:.2f} reais.\033[m
''')
