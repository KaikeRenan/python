# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A)Quantas pessoas foram cadastradas.
# B)Uma listagem com as pessoas mais pesadas.
# C)Uma listagem com as pessoas mais leves.

pessoas = []
dados = []

maior = menor = 0

while True:
    if len(pessoas) >= 1:
        print('\n')
    
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1] 
        elif dados[1] < menor:
            menor = dados[1]
            
    pessoas.append(dados[:])
    
    dados.clear()
    
    opcao = ''
    opcao = str(input("Deseja cadastrar mais pessoas? (S/N): ")).strip().upper()[0]
    
    if opcao == 'N': 
        break        
    
print('\n')

for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]} Kg")
        
print('\n')

print(f"Foram cadastradas {len(pessoas)} pessoas")

print(f"Maior peso cadastrado foi {maior} Kg. Peso de ", end='')

for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f"{pessoa[0]} ", end='') 

print(f"\nMenor peso cadastrado foi {menor} Kg. Peso de ", end='')

for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f"{pessoa[0]} ", end='')