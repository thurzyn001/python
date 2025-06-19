from sys import exit
from time import sleep
from random import choice

try:
    def encerrar_programa():
        print('\033[1;31;48mEntrada inválida. Encerrando Programa.')
        exit()
    def jogar():
            pergunta1 = int(input('''Vamos jogar Pedra,papel ou tesoura?
        1 = \033[1;32;48mSim\033[m 2 = \033[1;31;48mNão\033[m
        '''))
            if pergunta1 < 1 or pergunta1 > 2:
                encerrar_programa()
            elif pergunta1 == 1:
                print('''
        Irei selecionar o que irei jogar
        e logo em seguida você digita sua o que irá jogar.
                        ''')
                lista = ['Pedra', 'Papel', 'Tesoura']
                escolha_pc = choice(lista)
        #carregamento fake
                print('selecionando.')
                sleep(0.5)
                print('selecionando..')
                sleep(0.5)
                print('selecionando...')
                pergunta2 = int(input('''Agora é sua vez. Escolha entre as opções abaixo.
        1 = Pedra 🪨 | 2 = Papel 📄 | 3 = Tesoura ✂️
        '''))
                if pergunta2 < 1 or pergunta2 > 3:
                    encerrar_programa()

        # empate pedra x pedra

                elif pergunta2 == 1 and escolha_pc == 'Pedra':
                    print('''
        Empate! 
        Jogador : Pedra 🪨 X 🪨 Pedra : Pc
                            ''')
        # derrota pedra x papel

                elif pergunta2 == 1 and escolha_pc == 'Papel':
                    print('''
        Perdeu!
        Jogador : Pedra 🪨 X 📄 Papel : Pc
                            ''')
        # vitoria pedra x tesoura

                elif pergunta2 == 1 and escolha_pc == 'Tesoura':
                    print('''
        Ganhou!
        Jogador : Pedra 🪨 X ✂️ Tesoura: Pc
                            ''')
        # vitoria papel x pedra

                elif pergunta2 == 2 and escolha_pc == 'Pedra':
                    print('''
        Ganhou!
        Jogador : Papel 📄 X 🪨 Pedra : Pc
                             ''')
        # empate papel x pedra

                elif pergunta2 == 2 and escolha_pc == 'Papel':
                    print('''
        Empate!
        Jogador : Papel 📄 X 📄 Papel : Pc
                                 ''')
        # empate papel x pedra

                elif pergunta2 == 2 and escolha_pc == 'Tesoura':
                    print('''
        Perdeu!
        Jogador : Papel 📄 X ✂️ Tesoura : Pc
                                     ''')
        # vitoria papel x pedra

                elif pergunta2 == 3 and escolha_pc == 'Pedra':
                    print('''
        Perdeu!
        Jogador : Tesoura ✂️ X 🪨 Pedra : Pc
                                 ''')
        # empate papel x pedra

                elif pergunta2 == 3 and escolha_pc == 'Papel':
                    print('''
        Ganhou!
        Jogador : Tesoura ✂️ X 📄 Papel : Pc
                                     ''')
        # empate papel x pedra

                elif pergunta2 == 3 and escolha_pc == 'Tesoura':
                    print('''
        Empate!
        Jogador : Tesoura ✂️ X ✂️ Tesoura : Pc
                            ''')
            elif pergunta1 == 2:
                print('Ok então. ಥ_ಥ')
                exit()
    jogar()
except ValueError:
    print('Entrada Inválida, Encerrando programa')
