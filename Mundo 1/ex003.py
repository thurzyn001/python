n1 = float(input('\033[4;38;2;0;255;127;48;2;0;100;100mDigite o primeiro número:\033[m'))
n2 = float(input('\033[4;38;2;221;160;221;48;2;138;43;226mDigite o segundo número:\033[m'))
s = n1 + n2

# Mistura dos tons de ciano e roxo na resposta final
print(f'\033[1;38;2;0;255;127mA soma entre \033[38;2;221;160;221m{n1}\033[27m e \033[38;2;221;160;221m{n2}\033[38;2;0;255;127m é igual a \033[38;2;138;43;226m{s}\033[m')
