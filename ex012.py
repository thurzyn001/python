valori = float(input('\033[38;2;255;182;193mQual o preço do produto que deseja calcular o desconto? R$\033[m '))
porcentdes = float(input('\033[38;2;255;182;193mQual a porcentagem de desconto do cupom?\033[m '))

valordes = (porcentdes * valori) / 100
valorf = valori - valordes

print(f'''
\033[38;2;255;182;193mO produto custa R${valori:.2f} reais.\033[m
\033[38;2;255;182;193mO cupom aplicado confere {porcentdes}% de desconto.\033[m
\033[38;2;255;182;193mNeste caso, o valor do desconto aplicado será de R${valordes:.2f} reais.\033[m
\033[38;2;255;182;193mE o valor final do produto após desconto é de R${valorf:.2f} reais.\033[m
''')

