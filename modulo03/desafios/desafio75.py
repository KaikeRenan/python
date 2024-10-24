# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.
    
numeros = (int(input("Digite um valor: ")),
           int(input("Digite outro valor: ")),
           int(input("Digite mais um valor: ")),
           int(input("Digite o último valor: ")))
    
print(f"Números inseridos foram:",end='')
for n in numeros:
    print(f" {n} ", end='')
    
print(f"\nnúmero 9 apareceu {numeros.count(9)} {'vez' if numeros.count(9) == 1 else 'vezes'}")

if 3 in numeros:
    print(f"o valor 3 foi inserido na posição {numeros.index(3)+1}ª")
else:
    print("o valor 3 não foi inserido")
    
print("os valores pares inseridos foram: ",end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')