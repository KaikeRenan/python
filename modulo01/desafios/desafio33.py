# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

# if num1 > num2 and num1 > num3:
#     print(f'O maior valor digitado foi {num1}')

# if num2 > num1 and num2 > num3:
#     print(f'O maior valor digitado foi {num2}')
    
# if num3 > num1 and num3 > num2:
#     print(f'O maior valor digitado foi {num3}')
    
# if num1 < num2 and num1 < num3:
#     print(f'O menor valor digitado foi {num1}')

# if num2 < num1 and num2 < num3:
#     print(f'O menor valor digitado foi {num2}')

# if num3 < num1 and num3 < num2:
#     print(f'O menor valor digitado foi {num3}')

menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num2<num3:
    menor = num3
print(f'O menor valor digitado foi {menor}')

maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num2 and num2>num3:
    maior = num3
print(f'O maior valor digitado foi {maior}')


