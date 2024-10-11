# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

contador_idade = 0
contador_homens = 0
contador_mulher_menos_20 = 0

while True:
    idade = int(input("Digite a idade: "))
    if idade > 18:
        contador_idade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("Digite o sexo (M/F): ").strip().upper()[0]
    if sexo == 'M':
        contador_homens += 1
    if idade < 20 and sexo == 'F':
        contador_mulher_menos_20 += 1
    op = ' '
    while op  not in 'SN':
        op = str(input("\nQuer continuar? (S/N): ")).strip().upper()[0]
    print("\n")
    if op == "N":
        break
    
print(f"Pessoas tem mais de 18 anos: {contador_idade}")
print(f"Homens foram cadastrados: {contador_homens}")
print(f"Mulheres tem menos de 20 anos: {contador_mulher_menos_20}")
    
    