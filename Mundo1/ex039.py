from datetime import datetime, timedelta

def ultimo_dia_util_junho(ano):
    # Define o último dia de junho
    ultimo_dia_junho = datetime(ano, 6, 30)

    # Ajusta para o último dia útil caso 30 de junho caia no final de semana
    if ultimo_dia_junho.weekday() == 5:  # Sábado
        ultimo_dia_junho -= timedelta(days=1)
    elif ultimo_dia_junho.weekday() == 6:  # Domingo
        ultimo_dia_junho -= timedelta(days=2)

    return ultimo_dia_junho


# Entrada do usuario
data_nascimento = input("Digite sua data de nascimento (formato: DD/MM/AAAA): ")
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

# Calcula a data em que completa 18 anos
data_18_anos = datetime(data_nascimento.year + 18, data_nascimento.month, data_nascimento.day)

# Determina o último dia útil de junho do ano em que completa 18 anos
ultimo_dia_util = ultimo_dia_util_junho(data_18_anos.year)

# Data atual
data_atual = datetime.now()

# Formata as datas no formato dia/mês/ano
data_formatada_ultimo_dia_util = ultimo_dia_util.strftime('%d/%m/%Y')

# Verifica se o usuario já completou 18 anos, se está no ano de alistamento, ou se ainda falta
if data_atual < data_18_anos:
    # Ainda não completou 18 anos
    print(f"Você deve se alistar até: {data_formatada_ultimo_dia_util}")
    tempo_restante = ultimo_dia_util - data_atual
    print(f"Faltam {tempo_restante.days} dias para o seu alistamento.")
elif data_atual < ultimo_dia_util:
    # Está no ano de alistamento
    tempo_restante = ultimo_dia_util - data_atual
    print(f"Você tem {tempo_restante.days} dias restantes para se alistar.")
elif data_atual == ultimo_dia_util:
    # Último dia para alistamento
    print("Hoje é o último dia para o seu alistamento!")
else:
    # Passou do prazo de alistamento
    atraso = data_atual - ultimo_dia_util
    print(f"Você está atrasado para o alistamento militar em {atraso.days} dias.")
