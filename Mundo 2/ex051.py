from subprocess import run

def limpar_tela():
    run(["cls"], shell=True)

def pa(inicio, termos, razao):

    sequencia = []

    for i in range(inicio, termos * razao + inicio, razao):
        sequencia.append(i)

    return sequencia

def cabecalho(msg):

    linha = "=" * len(msg)
    print(linha)
    print(msg)
    print(linha)
    print("")

def start():

    limpar_tela()

    cabecalho("Progressão Aritmética v.1.0")

    inicio = int(input("Digite o primeiro termo da PA: "))
    print("")   
    termos = int(input("Digite a quantidade de termos da PA: "))
    print("")
    razao = int(input("Digite a razão da PA: "))
    print("")

    resultado = pa(inicio, termos, razao)

    cabecalho(f"PA de {termos} termos, com início em {inicio} e razão de {razao}:")

    print(" → ".join(map(str, resultado)) + " → Fim da PA.")

start()
