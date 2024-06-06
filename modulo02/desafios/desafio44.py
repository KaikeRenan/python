# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço normal 

# – 3x ou mais no cartão: 20% de juros

print(f'{'LOJAS ALMEIDA':=^40}') #centralizado em 40 espaços

preço_compras = float(input('Qual o valor do produto? R$'))

print('=-'*30)

print("""Formas de pagamento
      
Digite (1) para pagar à vista dinheiro/cheque ganhe 10% de desconto 

Digite (2) para pagar à vista no cartão ganhe 5% de desconto

Digite (3) para pagar 2x no cartão

Digite (4) para pagar 3x ou mais no cartão com 20% de juros""")

escolha = int(input('\nQual a forma de pagamento voce deseja escolher? '))

print('=-'*30)

if escolha == 1:
    print(f'Sua compra de R${preço_compras:.2f} vai custar R${preço_compras-(preço_compras*10/100):.2f} no final')
elif escolha == 2:
    print(f'Sua compra de R${preço_compras:.2f} vai custar R${preço_compras-(preço_compras*5/100):.2f} no final')
elif escolha == 3:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${preço_compras/parcelas:.2f}')
    print(f'Sua compra de R${preço_compras:.2f} vai custar R${preço_compras:.2f} no final ')
elif escolha == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${(preço_compras+(preço_compras*20)/100)/parcelas:.2f} COM JUROS')
    print(f'Sua compra de R${preço_compras:.2f} vai custar R${preço_compras+(preço_compras*20/100):.2f} no final')
else:
    print('\033[31mOpção invalida de pagamento. Tente novamente!!!\033[m')
    