c = float(input('\033[38;2;173;216;230mDigite a temperatura em Celsius:\033[m '))
f = (c * 1.8) + 32
k = c + 273.15

print(f'''
\033[38;2;173;216;230mA temperatura de {c}°C equivale a:\033[m
\033[38;2;255;99;71m{f:.2f}°F\033[m
\033[38;2;144;238;144m{k:.2f} K\033[m
''')
