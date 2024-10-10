# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8 

n = int(input("Quantos termos você quer mostrar: "))
primeiro = 0
segundo = 1
c = 3

print(f"{primeiro} - {segundo} - ", end='')

while c <= n:
    aux = primeiro + segundo
    primeiro = segundo
    segundo = aux
    c += 1
    print(f"{aux} - ", end='')
print("- FIM")
 