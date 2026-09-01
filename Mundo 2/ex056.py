from subprocess import run

def limpar_tela():
    run(["cls"], shell=True)

def mostra_cabecalho(msg):
    linha = "=" * len(msg)
    print(f"{linha}\n{msg}\n{linha}\n")

def defini_loop():
    return int(input("Quantidade de pessoas que serão analisadas: "))

def cadastrar_pessoas(num):
    lista_pessoas = []  

    for i in range(num):
        nome = input(f"Digite o nome da {i + 1}ª pessoa: ").strip().title()
        idade = int(input(f"Digite a idade de {nome}: "))
        sexo = input(f"Digite o sexo de {nome} [M/F]: ").strip().upper()
        print("")

        pessoa = {
            "nome": nome,
            "idade": idade,
            "sexo": sexo
        }

        lista_pessoas.append(pessoa)

    return lista_pessoas

def obter_extremos(lista):
    """Retorna o objeto da pessoa mais velha e da mais nova em uma lista."""
    if not lista:
        return None, None
    mais_velha = max(lista, key=lambda p: p["idade"])
    mais_nova = min(lista, key=lambda p: p["idade"])
    return mais_velha, mais_nova

def analisar_e_exibir_pessoas(lista_pessoas):
    if not lista_pessoas:
        print("Nenhuma pessoa cadastrada.")
        return

    homens = [p for p in lista_pessoas if p["sexo"] == "M"]
    mulheres = [p for p in lista_pessoas if p["sexo"] == "F"]

    h_velho, h_novo = obter_extremos(homens)
    m_velha, m_nova = obter_extremos(mulheres)
    p_velha, p_nova = obter_extremos(lista_pessoas)

    media_idade = sum(p["idade"] for p in lista_pessoas) / len(lista_pessoas)
    h_sub20 = sum(1 for p in homens if p["idade"] < 20)
    m_sub20 = sum(1 for p in mulheres if p["idade"] < 20)

    limpar_tela()

    mostra_cabecalho("    Resultado da análise:   ")

    mostra_cabecalho("    Geral:   ")

    print(f"• Média de idade do grupo: {media_idade:.1f} anos")
    print(f"• Pessoa mais velha no geral: {p_velha['nome']} ({p_velha['idade']} anos)")
    print(f"• Pessoa mais nova no geral:  {p_nova['nome']} ({p_nova['idade']} anos)")
    print("")

    mostra_cabecalho("    Homens:   ")

    if homens:
        print(f"• Homem mais velho: {h_velho['nome']} ({h_velho['idade']} anos)")
        print(f"• Homem mais novo:  {h_novo['nome']} ({h_novo['idade']} anos)")
        print(f"• Homens com menos de 20 anos: {h_sub20}")
    else:
        print("• Nenhum homem foi cadastrado.")
    print("")

    mostra_cabecalho("    Mulheres:   ")

    if mulheres:
        print(f"• Mulher mais velha: {m_velha['nome']} ({m_velha['idade']} anos)")
        print(f"• Mulher mais nova:  {m_nova['nome']} ({m_nova['idade']} anos)")
        print(f"• Mulheres com menos de 20 anos: {m_sub20}")
    else:
        print("• Nenhuma mulher foi cadastrada.")
    print("")

def main():
    num = defini_loop()
    print("")
    lista_pessoas = cadastrar_pessoas(num)
    analisar_e_exibir_pessoas(lista_pessoas)

def start():
    limpar_tela()
    mostra_cabecalho("   Analisador de pessoas v.1.0   ")
    main()

start()
