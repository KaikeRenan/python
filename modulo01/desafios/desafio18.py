# crie um código que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians

ang = float(input('Digite o valor do angulo: °'))

rad = radians(ang)

seno = sin(rad)
coss = cos(rad)
tang = tan(rad)

print(f'O valor do seno é: {seno:.2f}\nO valor do cosseno é: {coss:.2f}\nO valor da tangente é {tang:.2f}')