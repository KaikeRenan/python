# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

soma = 0
maior_idade = 0
mais_velho = ''
qt_mulheres = 0

for loop in range(1,5):
    nome = str(input(f"Digite o nome da {loop}° pessoa: ")).strip()
    idade = int(input(f"Digite a idade da {loop}° pessoa: "))
    sexo = str(input(f"Digite o sexo da {loop}° pessoa: ")).strip().upper()
    print('\n')
    
    soma += idade
    
    if loop == 1 and sexo == 'MASCULINO':
        maior_idade = idade
        mais_velho = nome
    else:
        if idade > maior_idade and sexo == 'MASCULINO':
            maior_idade = idade
            mais_velho = nome
        
    if sexo == "FEMININO" and idade < 20:
        qt_mulheres += 1
        
media = soma / 4

print("\n")
print(f"Média de idade do grupo: {media:.2f} anos")
print(f"O homem mais velho tem {maior_idade} anos e se chama {mais_velho}")
print(f"Ao todo são {qt_mulheres} mulheres com menos de 20 anos")