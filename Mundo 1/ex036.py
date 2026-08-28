from sys import exit

try:
    valor = float(input('Valor do Imóvel: '))
    if valor <= 0:
        print('O imóvel não pode ter valor de zero R$ ou negativo.')
        exit()
    sal = float(input('Salário Atual: '))
    if sal <= 0:
        print('Você também não pode ter um salário de zero R$ ou negativo.')
        exit()
    anos = float(input('Em quantos anos você deseja quitar a divida? '))
    if anos < 1:
        print('O número minimo de anos para o parcelamento é 1.')
        exit()
    else:
        par = anos * 12
        valorpar = valor / par
        porcentparcela = (valorpar / sal) * 100
        print(f'''
O valor do imóvel é R${valor:.2f} reais, que será dividido em
{par} parcelas de R${valorpar:.2f} reais cada.
Isso equivale a {porcentparcela:.2f}% do seu salário.
informamos isso pois se o valor da parcela exceder o equivalente
a 30% do seu salário, o finaciamento é automaticamente negado.''')
        if porcentparcela > 30:
            print(f'''
A parcela representa {porcentparcela:.2f}% do seu salário, o que excede o limite de 30%.
O financiamento será negado.''')
        else:
            print('Financiamento Aprovado. Parabéns!')
except ValueError:
    print('Digite apenas valores.')
