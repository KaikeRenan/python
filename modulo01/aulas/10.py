# nome = str(input('Qual é seu nome: '))
# if nome == 'Kaike':
#     print('Que nome lindo voce tem!')
# else:
#     print('Seu nome é tao normal!')
# print(f'Bom dia, {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
# if m >= 6.0:
#     print('Sua média foi boa! PARABENS!')
# else:
#     print('Sua média foi ruim! ESTUDE MAIS!')
print('PARABENS' if m >= 6.0 else 'ESTUDE MAIS')