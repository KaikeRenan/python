#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários

from moeda import resumo
from dado import leia_dinheiro

num = leia_dinheiro("Digite o preço: R$")
aumento = int(input("Digite quantos % quer aumentar o preço: "))
desconto = int(input("Digite quantos % quer descontar do preço: "))
print(resumo(num, aumento, desconto))

