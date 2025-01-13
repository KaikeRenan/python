# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome='<desconhecido>', gols=0):
    return f"O jogador {nome} marcou {gols} gols"
    
jogador_nome = str(input("Digite o nome do jogador: "))
jogador_gols = str(input("Digite a quantidade de gols marcados: "))
if jogador_gols.isnumeric():
    jogador_gols = int(jogador_gols)
else:
    jogador_gols = 0
if jogador_nome.strip() == '':
    print(ficha(gols=jogador_gols,))
else:
    print(ficha(jogador_nome, jogador_gols))