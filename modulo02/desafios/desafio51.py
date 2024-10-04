# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

termo = float(input('Digite o primeiro termo da PA: '))

razao = float(input('Digite a razão da PA: '))

for i in range(10):
    print(f'{i+1}° Termo : {termo + (i*razao)}')
    