cidade = str(input('\033[38;2;150;50;250mDigite o nome da cidade: \033[m')).strip().lower()
print(f'\033[38;2;150;50;250mA cidade começa com a palavra Santo: {cidade.startswith("santo")}\033[m')


#Código do Guanabara:
#cid = str(input('digite o nome da cidade: ').strip())
#print(f' A cidade começa com a palavra Santo: {cid[:5].upper() == 'SANTO'}')
