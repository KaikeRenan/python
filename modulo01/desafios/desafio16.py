# crie um código que leia um número qualquer pelo teclado e mostre na tela a sua porçao inteira 
# ex: digite um número: 6.127 - o número 6.127 tem a parte inteira 6

from math import trunc

num = float(input('Digite um número: '))

print(f'O número {num} tem a parte inteira {trunc(num)}')

# print(f'O número {num} tem a parte inteira {int(num)}')