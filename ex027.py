nome = str(input('\033[38;2;150;100;255mDigite seu nome completo: \033[m')).strip()
lista = nome.split()
print(
f'''
\033[38;2;100;200;150mMuito prazer em te conhecer!
Seu primeiro nome é: {lista[0].capitalize()}.
Seu último nome é: {lista[-1].capitalize()}.\033[m'''
)
