try:
    ano = int(input('\033[38;2;100;149;237mDigite um ano para saber se ele é bissexto: \033[m'))

    if ano < 0:
        ano_pos = -ano  # Converte para positivo
        tipo = 'a.C'
    else:
        ano_pos = ano
        tipo = 'd.C'

    if (ano_pos % 4 == 0 and ano_pos % 100 != 0) or (ano_pos % 400 == 0):
        print(f'\033[38;2;0;128;0mO ano {ano_pos}{tipo} é bissexto.\033[m')
    else:
        print(f'\033[38;2;255;0;0;47mO ano {ano_pos}{tipo} não é bissexto.\033[m')

except ValueError:
    print('\033[38;2;255;165;0mEntrada inválida! Por favor!, digite um ano válido (apenas números).\033[m')
