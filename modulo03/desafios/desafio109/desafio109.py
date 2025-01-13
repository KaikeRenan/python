#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108

from moeda import metade, dobro, diminuir, aumentar, moeda

num = float(input("Digite o preço: R$"))

print(f"A metade de {moeda(num)} é {metade(num, True)}")
print(f"o dobro de {moeda(num)} é {dobro(num, True)}")

aumento = int(input("Digite quantos % quer aumentar o preço: "))
print(f"Aumentando {aumento}% de {moeda(num)} temos {aumentar(num, aumento, True)}")

desconto = int(input("Digite quantos % quer descontar do preço: "))
print(f"Descontando {desconto}% de {moeda(num)} temos {diminuir(num, desconto, True)}")