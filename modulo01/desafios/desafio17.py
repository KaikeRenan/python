# crie um código que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa 

from math import hypot

co = float(input('Digite o comprimento do cateto oposto: ')) 
ca = float(input('Digite o comprimento do cateto adjacente: '))

# hipotenusa = (co**2 + ca**2) ** 1/2
hipotenusa = hypot(co, ca)

print(f'O comprimento da hipotenusa é: {hipotenusa:.2f}')