# Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Informe um número: '))

print(f"""Unidade: {num//1%10}
Dezena: {num//10%10}
Centena: {num//100%10}
Milhar: {num//1000%10}""")

# num = int(input('Informe um número: '))
# n = str(num)

# print(f"""Unidade: {num[3]}
# Dezena: {num[2]}
# Centena: {num[1]}
# Milhar: {num[0]}""")