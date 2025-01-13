# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

dados = []

pessoa = {}

soma_idades = 0

while True:
    pessoa.clear()
    
    pessoa['nome'] = str(input("Digite seu nome: "))
    
    while True:
        pessoa['sexo'] = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO!!! Por favor, digite apenas M ou F.")
        
    pessoa['idade'] = int(input("Digite sua idade: "))
    
    soma_idades += pessoa['idade']

    dados.append(pessoa.copy())
    
    while True:
        op = str(input("Deseja cadastrar mais pessoas? (S/N): ")).strip().upper()[0]
        if op in 'SN':
            break
        print("ERRO!!! Responda apenas S ou N.")
        
    if op == "N":
        break
    
print()

print(f"Quantidade de pessoas cadastradas: {len(dados)}")

media = soma_idades/len(dados)
print(f"Média de idades: {media:5.2f} anos")

print("Mulheres cadastradas: ", end='')
for p in dados:
    if p['sexo'] in "Ff":
        print(f"{p['nome']}, ", end='')
        
print()

print("Pessoas com idade acima da média: ")
for p in dados:
    if p['idade'] >= media:
        print('   ', end='')
        for keys, values in p.items():
            print(f"{keys} = {values}; ", end='')
        print()
        
print("<< Encerrado >>")
