# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

soma = 0
cont = 0

for c in range(0,6):
    num = int(input(f"Digite o {c}° valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1
    
print(f"Você informou {cont} números e a soma é {soma}")
