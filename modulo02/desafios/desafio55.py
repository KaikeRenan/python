# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

maior_peso = 0
menor_peso = 0

for loop in range(1,6):
    peso = float(input(f"Peso da {loop}° pessoa: "))
    
    if loop == 1:
        maior_peso = peso
        menor_peso = peso
    else: 
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
    
print(f"O maior peso lido foi de {maior_peso:.2f} kg\nO menor peso lido foi de {menor_peso:.2f} kg")