# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# import moeda
from moeda import metade, dobro, diminuir, aumentar

num = float(input("Digite o preço: R$"))

# metade = moeda.metade(num)
# dobro = moeda.dobro(num)
# diminui = moeda.diminuir(num)
# aumento = moeda.aumentar(num)

print(f"A metade de R${num:.2f} é R${metade(num):.2f}")
print(f"o dobro de R${num:.2f} é R${dobro(num):.2f}")

aumento = int(input("Digite quantos % quer aumentar o preço: "))
print(f"Aumentando {aumento}% de R${num:.2f} temos R${aumentar(num, aumento):.2f}")

desconto = int(input("Digite quantos % quer descontar do preço: "))
print(f"Descontando {desconto}% de R${num:.2f} temos R${diminuir(num, desconto):.2f}")