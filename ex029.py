try:
    vel = float(input('\033[38;2;100;150;255mQual a velocidade do carro? \033[m'))
    if vel < 0:
        print('\033[38;2;255;0;0mComo? Só como?\033[m')
    elif vel == 0:
        print('\033[38;2;0;255;0mAí você está parado né? durrrr!\033[m')
    elif vel <= 80:
        print('\033[38;2;100;255;100mDentro da velocidade permitida. Tudo certo!\033[m')
    else:
        print(f'''\033[38;2;255;100;0m
    Ei seu pilantra! A velocidade permitida é no máximo 80Km/h!
    Você passou a {vel}Km/h, {vel-80}Km/h acima do limite permitido.
    A multa é de R$7,00 por Km/h acima do permitido, totalizando R${(vel-80) * 7:.2f}.
    de multa a serem pagos pra mim, aceito dinheiro, Pix, Débito, Crédito,
    Xerecard entre diversos outros. E pague logo que eu to com pressa!\033[m''')
except ValueError:
    print('\033[38;2;255;0;0mEntrada inválida! Digite apenas números (sem letras ou símbolos).\033[m')
