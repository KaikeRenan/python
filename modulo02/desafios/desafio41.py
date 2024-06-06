# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER

from datetime import date

ano = int(input('Em que ano voce nasceu? '))

idade = date.today().year - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos\nClassificaçao: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos\nClassificaçao: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos\nClassificaçao: JÚNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos\nClassificaçao: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos\nClassificaçao: MASTER')