# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split() #separa

tudo_junto = ''. join(palavras) #junta

# inverso = ''

# for letra in range(len(tudo_junto) - 1, -1, -1):
#     inverso += tudo_junto[letra]

inverso = tudo_junto[::-1]

print(f"O inverso de {tudo_junto} é {inverso}")

if inverso == tudo_junto:
    print("Temos um palíndromo")
else:
    print("A frase digitada não é um palíndromo")

