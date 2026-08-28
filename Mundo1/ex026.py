frase = str(input('\033[38;2;100;200;255mDigite uma frase qualquer: \033[m')).strip().lower()
print(
    f'''
\033[38;2;150;50;250mA quantidade de letras 'A' em "{frase}" é {frase.count('a') + frase.count('ã')}.\033[m
\033[38;2;150;50;250mA primeira vez que a letra aparece é na posição: {frase.find('a') + 1}.\033[m
\033[38;2;150;50;250mE a última vez é na posição: {frase.rfind('a') + 1}.\033[m'''
)
