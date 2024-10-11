# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

# situacao_num = ' '

print("Vamos jogar par ou ímpar\n")

v = 0

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0,10)
    total = jogador+computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? ")).strip().upper()    
    print(f"\nVocê jogou {jogador} e o computador jogou {computador}. Total é {total} ",end='')
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == 'P':
        if total % 2 == 0:
            print("\nVocê VENCEU!")
            v += 1
        else:
            print("\nVocê PERDEU!")
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print("\nVocê VENCEU!")
            v += 1
        else:
            print("\nVocê PERDEU!")
            break
    print("\nVamos jogar novamente...\n")
print(f"\nGAME OVER! Você venceu {v} vezes")
    
    # num = int(input("Digite um valor entre 0 e 10: "))
    # escolha_usuario = str(input("Digite sua escolha? (P/I) ")).strip().upper()
    
    # num_pc = randint(0,10)
    # total = num+num_pc
    # if total % 2 == 0:
    #     situacao_num = 'PAR' 
    # else:
    #     situacao_num = 'ÍMPAR'
        
    # print(f"\nVocê jogou {num} e o computador jogou {num_pc}. Total é {total} e é {situacao_num}\n")
    
    # if escolha_usuario == 'P':
    #     escolha_usuario = 'PAR'
    #     escolha_pc = 'I'
    # elif escolha_usuario == 'I':
    #     escolha_usuario = 'ÍMPAR'
    #     escolha_pc = 'P'
        
    # if escolha_usuario == situacao_num:
    #     print("Você VENCEU!\nVamos jogar novamente...")
    # else:
    #     print("Você PERDEU!\n")
    #     break
