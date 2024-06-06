# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))

print(f"""\nVoce quer converter o número {num} para qual base?
Digite 1 para binário
Digite 2 para octal 
Digite 3 para hexadecimal.\n""")

escolha = int(input('Qual a sua escolha? '))

if escolha == 1:
    print(f'\nO número {num} convertido para a base binária é igual a: {bin(num)[2:]}')
elif escolha == 2:
    print(f'\nO número {num} convertido para a base octal é igual a: {oct(num)[2:]}')
elif escolha == 3:
    print(f'\nO número {num} convertido para a base hexadecimal é igual a: {hex(num)[2:]}')
else:
    print('\nOpção inválida') 