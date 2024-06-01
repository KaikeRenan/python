# crie um código que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possíveis sobre ele

algo = input('Digite algo: ')
print(f'O tipo primitivo do que voce digitou é {type(algo)}')
print(f'É númerico: {algo.isnumeric()}')
print(f'É alfanumérico: {algo.isalnum()}')
print(f'É alfabético: {algo.isalpha()}')
print(f'É da tabela ASCII: {algo.isascii()}')
print(f'É decimal: {algo.isdecimal()}')
print(f'É dígito: {algo.isdigit()}')
print(f'É maiúsculo: {algo.isupper()}')
print(f'É minúsculo: {algo.islower()}')
print(f'É capitalizado: {algo.istitle()}')
print(f'Só tem espaços: {algo.isspace()}')