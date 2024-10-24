# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

numeros = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
            
print(f"Números sorteados foram:",end='')
for n in numeros:
    print(f" {n} ", end='')
print(f"\nO menor valor: {max(numeros)}")
print(f"O maior valor: {min(numeros)}") 