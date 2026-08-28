reais = float(input('\033[38;2;255;255;255;48;2;30;30;30mQuantos reais você tem em sua carteira? R$\033[m '))
moeda = str(input('\033[38;2;255;255;255;48;2;30;30;30mQual a moeda que você deseja comprar?\033[m '))
valor = float(input('\033[38;2;255;255;255;48;2;30;30;30mQual o valor desta moeda em reais?\033[m '))

print(f'''
      \033[38;2;255;255;255;48;2;47;79;79mVocê tem R${reais:.2f} reais em sua carteira.\033[m
      Considerando o valor atual de \033[38;2;255;215;0m{moeda}\033[m que é de R${valor:.5f} reais.
      Você pode comprar aproximadamente \033[38;2;0;255;0m{reais/valor:.2f} {moeda}s.\033[m
      ''')
