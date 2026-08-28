from sys import exit

try:
    def encerrar_programa():
        print('Entrada invalida, Encerrando programa.')
        exit()
    valor = float(input('Digite o valor do produto em Reais. R$: '))
    if valor <= 0:
        encerrar_programa()
    selecao = int(input(f'''
Selecione uma das opções a seguir
1: Para Pagamento à vista em dinheiro/PIX (10% de desconto)
2: Para Pagamento à vista no cartão (5% de desconto)
3: Para parcelamento em até duas vezes sem juros
4: Para parcelamento em 3 ou mais (acréscimo de 20% e Máximo de 24 parcelas.)
'''))
    if selecao < 1 or selecao > 4:
        encerrar_programa()
    elif selecao == 1:
        desconto = (valor * 10 / 100)
        valor_final = valor - desconto
        print(f'''
Forma de pagamento: dinheiro/PIX.
Valor parcial: R$: {valor}.
Desconto: R$: {desconto}. (10%)
Valor final: R$: {valor_final}.      
                ''')
    elif selecao == 2:
        desconto = (valor * 5 / 100)
        valor_final = valor - desconto
        print(f'''
Forma de pagamento: À vista no cartão.
Valor parcial: R${valor}.
Desconto: R${desconto}. (5%)
Valor final: R${valor_final}.               
                ''')
    elif selecao == 3:
        valor_parcela = valor / 2
        print(f'''
Forma de pagamento: Parcelamento no cartão.
Número de parcelas: 2.
Valor da parcela: R${valor_parcela}.
Desconto: R$0,00.
Valor final: R${valor} em 2 vezes sem juros.
                ''')
    elif selecao == 4:
        numero_parcelas = int(input('Número de parcelas: '))
        if numero_parcelas < 0 or numero_parcelas > 24:
            encerrar_programa()
        else:
            acrescimo = valor * 20 / 100
            valor_final = valor + acrescimo
            valor_parcela = valor_final / numero_parcelas
            print(f'''
Forma de pagamento: Parcelamento no cartão
Número de parcelas: {numero_parcelas}.
Valor da parcela: R${valor_parcela:.2f}.
Acréscimo: R${acrescimo} (20%).
Valor final: R$:{valor_final} em {numero_parcelas} vezes com juros.
                    ''')
except ValueError:
    print('Entrada inválida. Encerrando programa.')