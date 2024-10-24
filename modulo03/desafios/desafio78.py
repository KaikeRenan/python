# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valores = []

for x in range(1,6):
    valores.append(int(input(f"Digite o {x}° valor: ")))
    
print(f"Lista dos valores digitados: {valores}")

print(f"O maior valor: {max(valores)} nas posições ", end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f"{i}...", end='')
        
print(f"\nO menor valor: {min(valores)} nas posições ", end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f"{i}...", end='')