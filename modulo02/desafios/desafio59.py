# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso. 

n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
op = 0

while op != 5:
    print("""
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
    """)
    
    op = int(input("Qual sua escolha? "))
    
    if op == 1:
        print(f"\nA soma dos valores {n1} e {n2} é igual a: {n1 + n2}")
    elif op == 2:
        print(f"\nA multiplicação dos valores {n1} e {n2} é igual a: {n1 * n2}")
    elif op == 3:
        if n1 > n2:
            print(f"\nEntre {n1} e {n2} o mair valor é: {n1}")
        elif n2 > n1:
            print(f"\nEntre {n1} e {n2} o maior valor é: {n2}")
        else:
            print(f"\nOs dois valores são iguais")
    elif op == 4:
        n1 = int(input("\nDigite o 1º novo valor: "))
        n2 = int(input("Digite o 2º novo valor: "))
    elif op == 5:
        print("\nFinalizando...")
        print("\nFim do programa! Volte sempre!")