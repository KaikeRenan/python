# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato. 

total_gasto = contador_mais_1000 = cont = 0

while True:
    nome_produto = str(input('Digite o nome do produto: '))
    preco_produto = float(input('Digite o preço do produto: R$ '))
    
    cont += 1
    
    total_gasto += preco_produto
    
    if preco_produto > 1000:
        contador_mais_1000 += 1
        
    if cont == 1 or preco_produto < menor_preco:
        menor_nome = nome_produto
        menor_preco = preco_produto

    op = ' '
    while op not in 'SN':
        op = str(input("Deseja continuar? (S/N): ")).strip().upper()[0]
    if op == 'N':
        break
    
print(f'Total da compra: R$ {total_gasto:.2f}')

print(f'Temos {contador_mais_1000} Produto{'s' if contador_mais_1000 > 1 else ''} que custam mais de R$1000')

print(f'Produto mais barato foi {menor_nome} que custa R$ {menor_preco:.2f}')
    