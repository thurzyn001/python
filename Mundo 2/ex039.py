from datetime import date

nasci = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nasci
if idade >= 1:
    print(f"Quem nasceu em {nasci} tem {idade} anos em {ano}.")

    if idade < 18:
        print(f"Ainda faltam {18 - idade} anos para o alistamento militar. \nSeu alistamento será em {ano + (18 - idade)}.")

    elif idade == 18:
        print(f"Está na hora de se alistar!")

    else:
        print(f"Seu alistamento militar foi em {ano - (idade - 18)}.")
