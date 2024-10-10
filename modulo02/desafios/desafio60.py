# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

# from math import factorial

# n = int(input("Digite um número: "))
# f = factorial(n)
# print(f"O fatorial de {n} é {f}")

n = int(input("Digite um número: "))
contador = n
f = 1

print(f"{n}! = ", end='')

while contador > 0:
    print(f"{contador}", end='')
    print(f" x " if contador > 1 else ' = ', end='')
    f *= contador #f = f * contador
    contador -= 1
print(f"{f}")
