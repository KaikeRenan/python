# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

dados = {}
partidas = []

dados['Nome'] = input("Nome do jogador: ")
qt_partidas = int(input(f"Quantas partidas {dados['Nome']} jogou? "))

for x in range(0, qt_partidas):
    partidas.append(int(input(f"Quantos gols na partida {x+1}? ")))

dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)

print()

print(dados)

print()

for keys, values in dados.items():
    print(f"O campo {keys} tem o valor {values}")

print()

print(f"O jogador {dados['Nome']} jogou {len(dados['Gols'])} partidas")

for i, values in enumerate(dados['Gols']):
    print(f"Partida {i+1}, fez {values} gols.")
    
print(f"Total de {dados['Total']} gols.")