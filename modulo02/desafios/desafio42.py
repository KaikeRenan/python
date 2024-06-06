# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

#ex35

print('Analisador de triângulos')

l1 = float(input('primeiro lado: ')) 
l2 = float(input('segundo lado: '))
l3 = float(input('terceiro lado: '))

if l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    # if l1 == l2 and l1 == l3 and l2 == l3:
    if l1 == l2 == l3:
        print('EQUILÁTERO: todos os lados iguais')
    elif l1 == l2 or l2 == l1 or l3 == l1 or l3 == l2:
        print('ISÓSCELES: dois lados iguais, um diferente')
    else:
    # if l1 != l2 != l3
        print('ESCALENO: todos os lados diferentes')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triângulo')