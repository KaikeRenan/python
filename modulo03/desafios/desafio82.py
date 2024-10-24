# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

valores = []

x = 1

print("Digite um número negativo para parar\n")

while True:
    valor = int(input(f"Digite o {x}° valor: "))
    valores.append(valor)
    x += 1
    if valor < 0:
        valores.pop()
        break
    
# valores_pares = [x for x in valores if x % 2 == 0]
# valores_impares = [x for x in valores if x % 2 == 1]

# valores_pares = valores[:]
# valores_impares = valores[:]

# for indice, valor in enumerate(valores_pares):
#     if valor % 2 != 0:
#         valores_pares.remove(valor)
        
# for indice, valor in enumerate(valores_impares):
#     if valor % 2 == 0:
#         valores_impares.remove(valor)

valores_pares = []
valores_impares = []

for indice, valor in enumerate(valores):
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)
    
print("Valores digitados: ", valores)

print("Valores pares: ", valores_pares)

print("Valores impares: ", valores_impares)