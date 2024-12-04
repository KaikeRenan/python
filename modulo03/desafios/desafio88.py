# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

# valores = [[],[],[],[],[],[]]

# num_sorteios = int(input("Quantos jogos quer que eu sorteie? "))

# for x in range(0, num_sorteios):
#     for y in range(0, 6):
#         valores[x].append(randint(1,60))    
        
#         valores[x].sort()
        
#     print(f"Jogo {x+1}: {valores[x]}")    

valores = []

jogos = []

contador = 0
total_jogos = 1

num_sorteios = int(input("Quantos jogos quer que eu sorteie? "))

while total_jogos <= num_sorteios:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in valores:
            valores.append(num)
            contador += 1
        if contador >= 6:
            break
        
    valores.sort()
    
    jogos.append(valores[:])
    
    valores.clear()
    
    total_jogos += 1

print('\n','-=' * 3, f'SORTEANDO {num_sorteios} JOGOS', '-=' * 3)
for i, v in enumerate(jogos):    
    print(f"Jogo {i+1}: {v}")
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)