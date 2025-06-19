# Cores do arco-íris em ANSI estendidas com fundo escuro e texto claro e legível
cores = [
    ("\033[48;5;52m\033[38;5;203m", "Vermelho"),   # Fundo vermelho escuro, texto vermelho claro
    ("\033[48;5;94m\033[38;5;214m", "Laranja"),    # Fundo laranja escuro, texto laranja claro
    ("\033[48;5;136m\033[38;5;229m", "Amarelo"),   # Fundo amarelo escuro, texto amarelo claro
    ("\033[48;5;22m\033[38;5;83m", "Verde"),       # Fundo verde escuro, texto verde claro
    ("\033[48;5;17m\033[38;5;45m", "Azul"),        # Fundo azul escuro, texto azul claro (ajustado)
    ("\033[48;5;54m\033[38;5;123m", "Anil"),       # Fundo anil escuro, texto anil claro
    ("\033[48;5;90m\033[38;5;183m", "Violeta"),    # Fundo violeta escuro, texto violeta claro
    ("\033[48;5;53m\033[38;5;218m", "Magenta"),    # Fundo magenta escuro, texto magenta claro
    ("\033[48;5;18m\033[38;5;87m", "Ciano")        # Fundo ciano escuro, texto ciano claro
]

# Input com cor do arco-íris, letra por letra (fundo escuro, texto claro)
texto_input = "Digite algo:"
input_colorido = ''.join(cores[i % len(cores)][0] + letra + "\033[m" for i, letra in enumerate(texto_input)) + " "
sla = input(f'{input_colorido}')  # Adiciona espaço sem cor

# Verificações
is_numero = sla.isnumeric() or (sla.count('.') == 1 and sla.replace('.', '').isnumeric())
is_alfa = all(palavra.isalpha() for palavra in sla.split())
is_alfanum = sla.isalnum()  # Corrigido para usar o método isalnum() corretamente
is_float = sla.count('.') == 1 and sla.replace('.', '').isdigit()
is_lower = sla.islower()
is_upper = sla.isupper()
is_space = sla.isspace()
is_title = sla.istitle()

# Impressão do resultado com cores (fundo escuro, texto claro e legível)
print(f'''
{cores[0][0]}O tipo primitivo de '{sla}' é: {type(sla)}\033[m
{cores[1][0]}'{sla}' é numérico: {'Verdadeiro' if is_numero else 'Falso'}\033[m
{cores[2][0]}'{sla}' é alfabético: {'Verdadeiro' if is_alfa else 'Falso'}\033[m
{cores[3][0]}'{sla}' é alfanumérico: {'Verdadeiro' if is_alfanum else 'Falso'}\033[m
{cores[4][0]}'{sla}' é um número com casas decimais: {'Verdadeiro' if is_float else 'Falso'}\033[m
{cores[5][0]}'{sla}' é somente minúsculo: {'Verdadeiro' if is_lower else 'Falso'}\033[m
{cores[6][0]}'{sla}' é somente maiúsculo: {'Verdadeiro' if is_upper else 'Falso'}\033[m
{cores[7][0]}'{sla}' só tem espaços: {'Verdadeiro' if is_space else 'Falso'}\033[m
{cores[8][0]}'{sla}' é um título: {'Verdadeiro' if is_title else 'Falso'}\033[m
\033[m
''')
