sali = float(input('\033[38;2;105;105;105mQual é o seu salário? R$:\033[m '))
porcentau = float(input('\033[38;2;105;105;105mQual é a porcentagem de aumento? %:\033[m '))
valorau = sali * porcentau / 100
salf = sali + valorau

print(f'''
\033[38;2;105;105;105mSeu salário atual corresponde a R${sali:.2f} reais.\033[m
\033[38;2;105;105;105mo aumento será de {porcentau}%.\033[m
\033[38;2;105;105;105mCalculando, chegamos ao valor de R${valorau:.2f} reais de aumento.\033[m
\033[38;2;105;105;105mPortanto, você passará a receber R${salf:.2f} reais a partir do próximo mês.
\033[38;2;105;105;105mParabéns!\033[m
     ''')
