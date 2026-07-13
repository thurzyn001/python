from math import sin, cos, tan, radians

ang = float(input('\033[38;2;173;216;230mDigite um ângulo qualquer para descobrir seu seno, cosseno e tangente:\033[m '))
rad = radians(ang)

print(
f'''
\033[38;2;173;216;230mO ângulo selecionado foi de: {ang}°.\033[m
\033[38;2;173;216;230mSeu seno corresponde a: {sin(rad):.3f}.\033[m
\033[38;2;173;216;230mSeu cosseno corresponde a: {cos(rad):.3f}.\033[m
\033[38;2;173;216;230mSua tangente corresponde a: {tan(rad):.3f}.\033[m
''')
