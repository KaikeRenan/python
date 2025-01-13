#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado

from moeda import metade, dobro, diminuir, aumentar, moeda

num = float(input("Digite o preço: R$"))

print(f"A metade de {moeda(num)} é {moeda(metade(num))}")
print(f"o dobro de {moeda(num)} é {moeda(dobro(num))}")

aumento = int(input("Digite quantos % quer aumentar o preço: "))
print(f"Aumentando {aumento}% de {moeda(num)} temos {moeda(aumentar(num, aumento))}")

desconto = int(input("Digite quantos % quer descontar do preço: "))
print(f"Descontando {desconto}% de {moeda(num)} temos {moeda(diminuir(num, desconto))}")