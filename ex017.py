from math import hypot

cato = float(input('\033[38;2;173;216;230mQual o comprimento em cm do cateto oposto? cm:\033[m '))
cata = float(input('\033[38;2;173;216;230mQual o comprimento em cm do cateto adjacente? cm:\033[m '))
print(f'''
\033[38;2;173;216;230mCateto oposto: {cato}cm.\033[m
\033[38;2;173;216;230mCateto adjacente: {cata}cm.\033[m
\033[38;2;173;216;230mHipotenusa: {hypot(cato, cata):.2f}cm.\033[m
    ''')
