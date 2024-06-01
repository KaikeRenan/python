# crie um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario_antigo = float(input('Digite o seu salário: R$'))

aumento = (salario_antigo*15)/100

salario_novo = salario_antigo + aumento

print(f'Seu salário era R${salario_antigo:.2f} e com o aumento de 15% ira para R${salario_novo:.2f}')