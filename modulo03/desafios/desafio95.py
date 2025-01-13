# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    
    jogador['Nome'] = input("\nNome do jogador: ")
    qt_partidas = int(input(f"\nQuantas partidas {jogador['Nome']} jogou? "))
    
    partidas.clear()

    for x in range(0, qt_partidas):
        partidas.append(int(input(f"Quantos gols na partida {x+1}? ")))

    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    
    time.append(jogador.copy()) #jogando a cópia do dicionario jogador para dentro da lista time
    
    while True:
        op = str(input("\nDeseja cadastrar mais pessoas? (S/N): ")).strip().upper()[0]
        if op in 'SN':
            break
        print("ERRO!!! Responda apenas S ou N.")
        
    if op == "N":
        break

print()

print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}",end='')
print()

for keys, values in enumerate(time):
    print(f"{keys:>3} ", end='')
    for value in values.values():
        print(f"{str(value):<15}", end='')
    print()

while True:
    busca = int(input("\nQuer ver os dados de qual jogador? (999 para parar): "))
    if busca == 999:
        print("\nFinalizando programa...")
        break
    if busca >= len(time):
        print(f"\nERRO!!! Jogador com código {busca} não encontrado")
    else:
        print(f"\nDados do jogador {time[busca]['Nome']}:")
        for i, g in enumerate(time[busca]['Gols']):
            print(f"Jogo {i+1} fez {g} gols.")