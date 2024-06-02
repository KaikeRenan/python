# o mesmo professor quer sortear a ordem de apresentaçao de trabalhos dos alunos, faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista_alunos)

print(f'A ordem sorteada será: {lista_alunos}')