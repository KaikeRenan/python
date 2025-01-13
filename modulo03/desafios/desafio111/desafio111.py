# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando

from desafio111.utilidadesCeV import moeda

num = float(input("Digite o preço: R$"))
aumento = int(input("Digite quantos % quer aumentar o preço: "))
desconto = int(input("Digite quantos % quer descontar do preço: "))
print(moeda.resumo(num, aumento, desconto))

