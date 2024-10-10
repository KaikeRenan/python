# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0] #somente a primeira letra

while sexo not in 'MmFf': #enquanto sexo não estiver em M ou F 
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
    
print(f"Sexo {'Masculino' if sexo == 'M'  else 'Feminino'} registrado com sucesso")
# print(f"Sexo {sexo} registrado com sucesso")
