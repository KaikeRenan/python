# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

n = 0
soma = 0
contador = 0

while n != 999:
    n = int(input('Digite um número (ou 999 para parar): '))
    if n != 999:
        contador += 1
    if n != 999:
        soma += n
print(f"Quantidade de números digitados {contador}")
print(f"A soma entre os números digitados {soma}")