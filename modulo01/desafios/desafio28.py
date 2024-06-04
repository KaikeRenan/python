# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep 

print('\n')

print('Vou pensar em um número entre 0 e 5. Tende adivinhar...')

num_pc = randint(0,5)

print('\n')

num_user = int(input('Em que número eu pensei? '))

print('Processando...')
sleep(2) #faz o computador esperar 2 segundos

if num_pc == num_user:
    print('PARABÉNS!! você conseguiu me vencer')
else:
    print(f'GANHEI! eu pensei no número {num_pc} e nao no {num_user}')
