from math import sqrt

n = float(input('\033[38;2;255;255;255;48;2;100;100;100mDigite um número :\033[m '))
print(f'''
\033[1;38;2;255;255;255;48;2;85;85;85mO número escolhido é: {n}.\033[m
\033[1;38;2;160;82;45;48;2;245;222;179mSeu Dobro é: {n * 2}.\033[m
\033[1;38;2;255;192;203;48;2;50;50;50mE seu Triplo é: {n * 3}.\033[m
\033[1;38;2;173;216;230;48;2;25;25;112mE sua raiz quadrada é {sqrt(n):.2f}.\033[m
      ''')
