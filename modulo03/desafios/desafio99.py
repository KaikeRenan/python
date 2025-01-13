# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(*valores):
    contador = maior = 0
    for valor in valores:
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    return maior
    
print(maior(1,20,3,4,5,10))
    