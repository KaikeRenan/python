# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input("Digite um número: "))

num_divi = 0

for c in range(1,num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        num_divi += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
    
print(f"\n\033[mO número {num} foi divisível {num_divi} vezes")
if num_divi == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele não é PRIMO!")
    