try:
    a = float(input('\033[38;2;100;149;237mDigite o comprimento da reta a: \033[m'))
    b = float(input('\033[38;2;100;149;237mDigite o comprimento da reta b: \033[m'))
    c = float(input('\033[38;2;100;149;237mDigite o comprimento da reta c: \033[m'))
    if a + b > c and a + c > b and b + c > a:
        print(f'''
\033[38;2;0;128;0mAs retas a, b e c com comprimentos {a}, {b} e {c} respectivamente,
podem formar um triângulo.\033[m''')
    else:
        print(f'''
\033[38;2;255;0;0mAs retas a, b e c com comprimentos {a}, {b} e {c} respectivamente,
não podem formar um triângulo.\033[m''')
except ValueError:
    print('''\033[38;2;255;0;0m
Comprimento inválido. Não utilize letras ou símbolos, apenas números.
Obs: Para números decimais utilize ponto no lugar de vírgula.\033[m''')
