# crie um código que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco_antigo = float(input('Digite o preço do produto: '))

desconto = (preco_antigo*5)/100
preco_novo = preco_antigo - desconto

print(f'O produto custava R${preco_antigo:.2f} e o novo preço com 5% de desconto será de R${preco_novo:.2f}')