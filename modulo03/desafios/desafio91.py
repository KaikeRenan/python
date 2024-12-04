# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}

ranking = []

print("Valores sorteados:")

for keys, values in jogo.items():
    print(f"{keys} tirou {values} no dado.")
    sleep(1)
    
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print()

print("Ranking dos jogadores:")
for indice, valores in enumerate(ranking):
    print(f"{indice+1}° lugar: {valores[0]} com {valores[1]}.")
    sleep(1)