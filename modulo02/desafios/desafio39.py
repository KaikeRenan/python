# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

sexo = str(input('Qual o seu sexo? F para feminino M para masculino: ')).strip().upper()

if sexo == 'F':
    print(f'Mulheres nao sao obrigadas a fazer parte do alistamento obrigatório')
else:
    ano = int(input('Em que ano voce nasceu? '))

    idade = date.today().year - ano
    idade2 = idade-18

    if idade < 18:
        print(f"""Quem nasceu em {ano} tem {idade} anos em {date.today().year}
Ainda faltam {18-idade} anos para o alistamento
seu alistamento será em {ano+18}""")
    elif idade == 18:
        print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}\nÉ a hora exata de se alistar')
    else:
        print(f"""Quem nasceu em {ano} tem {idade} anos em {date.today().year}
Voce já deveria ter se alistado há {idade2} anos
seu alistamento foi em {date.today().year - idade2}""")