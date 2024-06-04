# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Analisador de Triangulos')

seg1 = float(input('primeiro segmento: ')) 
seg2 = float(input('segundo segmento: '))
seg3 = float(input('terceiero segmento: '))

# lados = seg1 + seg2

# if seg1 < lados and seg2 < lados and seg3 < lados:

if seg1  < seg2+seg3 and seg2  < seg1+seg3 and seg3  < seg2+seg1:
    print('Os segmentos acima PODEM FORMAR um triangulo')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo')