# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

valores = []

c = 1

print("Digite um número negativo para parar\n")

while True:
    valor = int(input(f"Digite o {c}° valor: "))
    if valor in valores:
        print("Valor já existente na lista. Não será adicionado.")
    else:
        valores.append(valor)
        c += 1
    if valor < 0:
        valores.pop()
        break
    
valores.sort()
print(f"Lista dos valores digitados: {valores}")