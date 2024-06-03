# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em que cidade voce nasceu? ')).strip().upper()
lista = cidade.split()
print('SANTO' in lista[0])

# print(cidade[:5] == 'SANTO')