try:
    dis = float(input('\033[38;2;100;149;237mQual a distância que você irá viajar em kms? R: \033[m'))
    print(f'\033[38;2;100;149;237mVocê está prestes a iniciar uma viagem de {dis}Kms.\033[m')
    if dis == 0:
        print('\033[38;2;255;165;0mVc deve estar me testando, não é possível.\033[m')
    elif dis < 0:
        print('\033[38;2;255;0;0mHAHA, muito engraçado, Mr. piadocas!\033[m')
    elif dis <= 200:
        print(f'''
    \033[38;2;0;128;0mPara viagens até 200km, cobramos R$0,50 reais por Km percorrido.
    O total da sua passagem ficou em R${dis * 0.50:.2f} reais.\033[m''')
    else:
        print(f'''
    \033[38;2;0;191;255mPara viagens acima de 200km, cobramos R$0,45 reais por Km percorrido.
    O total da sua passagem ficou em R${dis * 0.45:.2f} reais.\033[m''')  # Azul claro
except ValueError:
    print('''\033[38;2;255;0;0m
    Entrada inválida, por favor, utilize apenas números
    (Não utilize letras ou símbolos) E para valores decimais como 130,50Km!
    Utilize um ponto no lugar da vírgula!\033[m''')
