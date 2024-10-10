# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
from time import sleep 

cont_palpites = 1

print('\nVou pensar em um número entre 0 e 10. Tende adivinhar...')

num_pc = randint(0,10)

num_user = int(input('\nEm que número eu pensei? '))

print('\nProcessando...')
sleep(2) #faz o computador esperar 2 segundos

while num_user != num_pc:
    if num_user < num_pc:
        print('\nVocê errou! O número que eu pensei é maior.')
    elif num_user > num_pc:
        print('\nVocê errou! O número que eu pensei é menor.')
    num_user = int(input("\nTente novamente. Em que número eu pensei? "))
    cont_palpites += 1

print(f'\nPARABÉNS!!! Você conseguiu me vencer\n{f"Você acertou de primeira" if cont_palpites == 1 else f'Você precisou de {cont_palpites} palpites para acertar'}')

# acertou = False
# palpites = 0
# while not acertou:
#     jogador = int(input("Qual é seu palpite? "))
#     palpites += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print("Mais... Tente mais uma vez.")
#         elif jogador > computador:
#             print("Menos... Tente mais uma vez.")
# print("Acertou com {palpites} tentativas. Parabéns!!!")