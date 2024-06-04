# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date #biblioteca para pegar a data da maquina

ano = int(input('Que ano deseja analisar?(digite 0 para analisar o ano atual): '))

if ano == 0:
    ano = date.today().year # ano atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else: 
    print(f'O ano {ano} nao é bissexto!')