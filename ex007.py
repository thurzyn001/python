n1 = float(input('\033[38;2;255;255;255;48;2;100;100;100mDigite a primeira nota:\033[m '))
n2 = float(input('\033[38;2;255;255;255;48;2;100;100;100mDigite a segunda nota:\033[m '))
print(f'\033[38;2;255;255;255;48;2;85;85;85mA média entre {n1:.2f} e {n2:.2f} é {(n1+n2)/2:.2f}.\033[m')
