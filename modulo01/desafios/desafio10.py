# crie um código que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar (US$1,00 = R$ 3,27)

carteira = float(input('Digite o quanto de dinheiro voce tem na carteira: R$'))

dolares = carteira/3.27

print(f'Convertendo para doláres voce tem US${dolares:.2f}')