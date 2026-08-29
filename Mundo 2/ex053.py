from subprocess import run

def limpar_tela():
    run(["cls"], shell=True)

def mostra_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def prepara_frase(frase):
    return frase.strip().upper().replace(" ", "")

def start():
    limpar_tela()
    mostra_cabecalho("É Palíndromo?? v.1.0")

    frase = input("Digite uma frase, para verificar se é um palíndromo: ")
    preparada = prepara_frase(frase)
    invertida = preparada[::-1]
    palindromo = preparada == invertida

    resultado = "é um palíndromo." if palindromo else "não é um palíndromo."

    print(f"\nA frase '{frase}', após remover espaços e colocar em maiúsculo "
        f"fica '{preparada}' e ao contrário fica '{invertida}', logo {resultado}")

start()
