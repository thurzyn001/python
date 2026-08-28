larg = float(input('\033[38;2;255;255;255;48;2;30;30;30mQual a largura em metros da parede que irá ser pintada?\033[m '))
alt = float(input('\033[38;2;255;255;255;48;2;30;30;30mQual a altura em metros da parede que deseja pintar?\033[m '))

print(f'''
\033[38;2;255;255;255;48;2;47;79;79mSua parede mede {larg} metros de largura e {alt} metros de altura,\033[m
\033[38;2;255;255;255;48;2;47;79;79mtotalizando uma área de {larg * alt}m².\033[m
\033[38;2;255;255;255;48;2;47;79;79mconsiderando que para cada metro quadrado(m²) a ser pintado,\033[m
\033[38;2;255;255;255;48;2;47;79;79mé necessário 0.5 litros de tinta, você irá precisar de aproximadamente:\033[m
\033[38;2;255;255;255;48;2;47;79;79m{(larg * alt) / 2} litros de tinta para pintar esta parede.\033[m
      ''')

