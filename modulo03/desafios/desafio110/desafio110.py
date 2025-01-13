#Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui

from moeda import resumo

num = float(input("Digite o preço: R$"))
aumento = int(input("Digite quantos % quer aumentar o preço: "))
desconto = int(input("Digite quantos % quer descontar do preço: "))
print(resumo(num, aumento, desconto))

