# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep 

lista = ['PEDRA','PAPEL','TESOURA']
escolha_pc = lista[random.randint(0,2)]

print(f'{'Vamos jogar Jokenpô':=^40}')

print("""Sua opçoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

escolha = int(input('Qual é a sua jogada? ')) 

if escolha > 2:
    print('\033[31mOpção Inválida. Tente novamente!!!\033[m')
else:
    escolha_jogador = lista[escolha]

    print('='*30)
    print('JO')
    sleep(.5)
    print('KEN')
    sleep(.5)
    print('PO!!!')
    sleep(.5)

    print('='*30)
    print(f'Computador jogou {escolha_pc}')
    print(f'Jogador jogou {escolha_jogador}')
    print('='*30)

    if escolha_jogador != escolha_pc:
        if escolha_jogador == 'PEDRA' and escolha_pc == 'TESOURA':
            print('\033[34mJOGADOR VENCEU\033[m')
        elif escolha_jogador == 'PAPEL' and escolha_pc == 'PEDRA':
            print('\033[34mJOGADOR VENCEU\033[m')
        elif escolha_jogador == 'TESOURA' and escolha_pc == 'PAPEL':
            print('\033[34mJOGADOR VENCEU\033[m')
        elif escolha_jogador == 'TESOURA' and escolha_pc == 'PEDRA':
            print('\033[31mCOMPUTADOR VENCEU\033[m')
        elif escolha_jogador == 'PEDRA' and escolha_pc == 'PAPEL':
            print('\033[31mCOMPUTADOR VENCEU\033[m')
        elif escolha_jogador == 'PAPEL' and escolha_pc == 'TESOURA':
            print('\033[31mCOMPUTADOR VENCEU\033[m')
    else:
        print('EMPATE')
    