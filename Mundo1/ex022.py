nome = str(input('\033[38;2;123;104;238mDigite seu nome completo: \033[m')).strip()
separa = nome.split()
print(f'''
\033[38;2;245;222;179mAnalisando seu nome:\033[m
\033[38;2;245;222;179mSeu nome somente em maiúsculas é {nome.upper()}.\033[m
\033[38;2;245;222;179mSeu nome somente em minúsculas é {nome.lower()}.\033[m
\033[38;2;245;222;179mSeu nome tem ao todo {len(nome) - nome.count(' ')} letras.\033[m
\033[38;2;245;222;179mSeu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.\033[m
    ''')
