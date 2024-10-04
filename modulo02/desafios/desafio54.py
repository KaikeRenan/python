#  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

ano_atual = date.today().year

qt_maiores = 0
qt_menores = 0

for c in range(1,8):
    ano_nascimento = int(input(f"Em que ano a {c}° pessoa nasceu? ")) 
    
    idade = ano_atual - ano_nascimento
    
    if idade < 18:
        qt_menores += 1
    else:
        qt_maiores += 1
        
print(f"\nAo todo tivemos {qt_maiores} pessoas maiores de idade\nE também tivemos {qt_menores} pessoas menores de idade")
