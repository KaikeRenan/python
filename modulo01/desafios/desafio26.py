# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

print(f"""A letra A aparece {frase.count('A')} vezes na frase.
A primeira letra A apareceu na posiçao {frase.find('A')+1}
A última letra A apareceu na posiçao {frase.rfind('A')+1}""")