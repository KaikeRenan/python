# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
# a) de 1 até 10, de 1 em 1                                                                                                                                              
# b) de 10 até 0, de 2 em 2                                                                                                                                           
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
        
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    
    contador = inicio
    
    if inicio < fim:
        while contador <= fim:
            print(f"{contador} ", end='', flush=True)
            sleep(0.5)
            contador += passo
        print("FIM!\n")
    else:
        while contador >= fim:
            print(f"{contador} ", end='', flush=True)
            sleep(0.5)
            contador -= passo
        print("FIM!\n")
        
contador(1, 10, 1)
contador(10, 0, 1)

print("\nPersonalize a contagem")
inicio_usuario = int(input("Digite o início: "))
fim_usuario = int(input("Digite o fim: "))
passo_usuario = int(input("Digite o passo: "))
contador(inicio_usuario, fim_usuario, passo_usuario)
