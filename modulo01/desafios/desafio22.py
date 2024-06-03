# Crie um programa que leia o nome completo de uma pessoa e mostre:
# nome em maiúsculas
# nome em minúsculas
# quantidade de letras que o nome tem ao todo
# qual primeiro nome e qual a quantida de letras

nome = str(input('Digite seu nome completo: '))
# nome = str(input('Digite seu nome completo: ')).strip()

lista = nome.split()

print(f"""Analisando seu nome...
Seu nome em maiúsculas é {nome.upper().strip()}
Seu nome em minúsculas é {nome.lower().strip()}
Seu nome tem ao todo {len(''.join(nome.strip()))} letras
Seu primeiro nome é {lista[0]} e ele tem {len(lista[0])} letras""")

# (len(nome) - nome.count(' ')) quantidade de letras que o nome tem ao todo
# {nome.find(' ')} quantidade de letras que o primiero nome tem

