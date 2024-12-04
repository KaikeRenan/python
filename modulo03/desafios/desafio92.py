# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import date

dados = {}

dados['Nome'] = input("Digite seu nome: ")

ano_nascimento = int(input("Digite o ano em que nasceu: "))
ano_atual = date.today().year
dados['Idade'] = ano_atual - ano_nascimento

dados['CTPS'] = int(input("Digite sua carteira de trabalho (0 não tem): "))

if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input("Em que ano você foi contratado? "))
    dados['Salário'] = float(input("Digite seu salário: R$"))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de Contratação'] + 35) - ano_atual)
else:
    dados['CTPS'] = 'Não tem'
    
for keys, values in dados.items():
    print(f"- {keys}: {values}")