# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

termo = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))

contador = 1

while contador <= 10:
    print(f'{contador}° Termo : {termo}')   
    termo += razao
    contador += 1
    
# primeiro = float(input("Primeiro termo: "))
# razao = float(input("Razão de PA: "))

# termo = primeiro 
# contador = 1

# while contador <= 10:
#     print(f"{termo} -> ", end='')
#     termo += razao
#     contador += 1
# print("FIM")
