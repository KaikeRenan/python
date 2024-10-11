# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

soma = 0
cont = 0
escolha = ' '

while escolha != 'N':
    n = int(input("Digite um número: "))
    escolha = str(input("Quer continuar? [S/N]: ")).strip().upper()
    soma += n
    cont += 1
    
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    
print(f"\nVocê digitou {cont} números e a média foi {soma/cont}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}")
