# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

import random
from time import sleep

def sorteia(lista):
    print("Sorteando os valores")
    for i in range(0,5):
        n = random.randint(0,100)
        lista.append(n)
        print(f"{n} ", end='', flush=True)
        sleep(0.3)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"\nSoma dos valores pares sorteados é {soma}")
        
valores = []
sorteia(valores)
somaPar(valores)
