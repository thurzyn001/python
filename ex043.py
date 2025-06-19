from sys import exit

def encerrar_programa():
    print('entrada inválida. Encerrando programa.')
    exit()
print('''
Seja bem vindo a calculadora de IMC (Índice de Massa Corporal)
Esta calculadora utiliza a fórmula base do IMC que é
                
                Peso(Kg)/Altura(M)²
        ''')
try:
    p = float(input('Por favor, digite seu peso em Kgs: '))
    if p <= 0:
        encerrar_programa()
    a =int(input('E agora a sua altura em Cms: '))
    if a <= 0:
        encerrar_programa()
    am = a / 100
    imc = p / (am * am)
    if imc < 18.5:
        print(f'''
Seu IMC é {imc}. Para IMCs menores que 18,5 é recomendado procurar um médico
para avaliação criteriosa do resultado. Pode indicar um estado
de consumo do organismo, com poucas reservas e riscos associados.
                ''')
    elif 18.5 <= imc <= 24.5:
        print(f'''
Seu IMC é {imc:.2f}. IMCs entre 18,5 e 24,9 são considerados o peso adequado.
Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros
da composição corporal, para compreender se estão dentro do recomendado.
Algumas pessoas apresentam IMC dentro da normalidade, mas tem circunferência
abdominal maior que a recomendada e/ou quantidade de massa gorda acima do ideal.
                ''')
    elif 25 <= imc < 29.9:
        print(f'''
Seu IMC é {imc:.2f}. IMCs entre 25 e 29,9 são considerados sobrepeso.
O sobrepeso está associado ao risco de doenças como diabetes e hipertensão.
Então, atenção! Consulte um médico e reveja hábitos para reverter o quadro.
Também é importante avaliar outros parâmetros, como a circunferência abdominal.
                ''')
    elif 30 <= imc < 34.9:
        print(f'''
Seu IMC é {imc:.2f}. IMCs entre 30 e 34,9 são considerados obesidade grau I.
è importante buscar orientação médica e nutricional para entender melhor
seu caso, mesmo que exames (colesterol e glicemia, por exemplo) estejam normais.
                    ''')
    elif 35 <= imc < 39.9:
        print(f'''
Seu IMC é {imc:.2f}. IMCs entre 35 e 39,9 são considerados obesidade grau II.
Indica um quadro de obesidade mais evoluído em relação a classificação
anterior e, mesmo com exames laboratoriais dentro da normalidade, não
se deve atrasar a busca por orientação médica e nutricional.  
                ''')
    elif imc >= 40:
        print(f'''
Seu IMC é {imc:.2f}. IMCs maiores que 40 são considerados obesidade grau III.
Nesse ponto, a chance de já estarmos diante de outras doenças associadas
é mais elevada. É fundamental buscar orientação médica.          
                ''')
except ValueError:
    print('''
Entrada Inválida.
Encerrando programa.
        ''')
