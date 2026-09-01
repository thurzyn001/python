from subprocess import run

def limpar_tela():
    run(["cls"], shell=True)

def mostra_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def defini_loop():
    num = int(input("Quantidade de pesos que serão digitados: "))
    return num

def verifica_peso(peso):
    menor = 0
    maior = 0
    for i in range(len(peso)):
        if peso[i] > maior:
            maior = peso[i]
        if peso[i] < menor or menor == 0:
            menor = peso[i]
    return maior, menor

def main():
    num = defini_loop()
    print("")
    peso = []

    for i in range(num):
        p = float(input(f"Digite o peso da {i + 1}ª pessoa: "))
        peso.append(p)

    maior, menor = verifica_peso(peso)
    print("")
    print(f"O maior peso digitado foi {maior:.2f}Kg e o menor foi {menor:.2f}Kg.")

def start():
    limpar_tela()
    mostra_cabecalho("Maior e menor peso v.1.0")
    main()

start()
