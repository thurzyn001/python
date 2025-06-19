nome = str(input('\033[38;2;100;200;255mDigite seu nome completo: \033[m')).lower().split()
print(f'\033[38;2;150;50;250mSeu nome tem "silva" em alguma posição: {"silva" in nome}\033[m')
