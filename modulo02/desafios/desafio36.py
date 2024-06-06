# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Quantos anos voce quer pagar? '))

meses = anos*12
prestacao_mensal = valor_casa/meses
salario30 = (salario*30)/100 #calculo de 30% do salário

# if prestacao_mensal >= salario30:
#     print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestaçao será de R${prestacao_mensal:.2f}\nEMPRÉSTIMO NEGADO')
# else:
#     print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestaçao será de R${prestacao_mensal:.2f}\nEMPRÉSTIMO pode ser CONCEDIDO')
    
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestaçao será de R${prestacao_mensal:.2f}')
if prestacao_mensal >= salario30:
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO CONCEDIDO')