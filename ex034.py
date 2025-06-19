try:
    sal = float(input('\033[38;2;100;149;237mQual é o seu salário? R$: \033[m'))
    if sal < 0:
        print('\033[38;2;255;0;0mVocê ta pagando pra trabalhar? Isso não é um funcionário, é um prefeito\033[m')
    elif sal == 0:
        print('\033[38;2;255;165;0mVocê nao ta ganhando nada pra trabalhar? Quem é seu chefe? O senhor Burnes?\033[m')
    elif sal > 1250:
        print(f'''
    \033[38;2;0;128;0mO aumento para salários acima de R$1250,00 reais é de 10%
    Você receberá \033[38;2;0;255;127m{sal + sal * 0.10:.2f}\033[m \033[38;2;0;128;0mreais a partir do próximo mês.\033[m''')
    else:
        print(f'''
    \033[38;2;0;128;0mO aumento para salários iguais ou inferiores a R$1250,00 reais é de 15%
    Você receberá \033[38;2;0;255;127m{sal + sal * 0.15:.2f}\033[m \033[38;2;0;128;0mreais a partir do próximo mês.\033[m''')
except ValueError:
    print('''
    \033[38;2;255;0;0mInválido: Não utilize símbolos ou letras e para valores decimais
    troque a vírgula por um ponto.\033[m
         ''')
