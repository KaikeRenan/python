# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.  
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []

x = 1

print("Digite um número negativo para parar\n")

while True:
    valor = int(input(f"Digite o {x}° valor: "))
    if valor in valores:
        print("Valor já existente na lista. Não será adicionado.")
    else:
        valores.append(valor)
        x += 1
    if valor < 0:
        valores.pop()
        break
    
print(f"Quantidade de valores que foram digitados: {len(valores)}")

valores.sort(reverse=True)

print(f"Lista na ordem decrescente: {valores}")

if 5 in valores:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")