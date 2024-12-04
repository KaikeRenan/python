# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

alunos = []

dados = []

contador = 0

while True:
    nome = str(input("Digite o nome do aluno: "))
    dados.append(nome)
    nota1 = float(input("Digite a primeira nota: "))
    dados.append(nota1)
    nota2 = float(input("Digite a segunda nota: "))
    dados.append(nota2)
    media = (nota1 + nota2) / 2
    dados.append(media)
    
    #alunos.append([nome], [nota1, nota2], [media])
    
    alunos.append(dados[:])
    
    dados.clear()
    
    opcao = ''
    opcao = str(input("Deseja adicionar mais alunos? (S/N): ")).strip().upper()[0]
    
    if opcao == 'N': 
        break 

print('\n','-=' * 5, 'BOLETIM', '=-'*5)
print(f"{"No.":<4}{"Nome":<10}{"Média":>8}")
for aluno in alunos:
    print(f"{contador:<4}{aluno[0]:<10}{aluno[3]:>8.2f}")
    contador += 1
    
print("\nDigite o número do aluno ou 999 para interromper")

while True:
    num = int(input("Deseja ver as notas de qual aluno? "))
    
    if num == 999:
        print("Finalizando...")
        break
    elif num <= len(alunos) - 1:
        print(f"Aluno: {alunos[num][0]} Nota 1: {alunos[num][1]:.2f} Nota 2: {alunos[num][2]:.2f}")
    else:
        print("Aluno não encontrado! Tente novamente")
    