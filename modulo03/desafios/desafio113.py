# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt, SystemExit):
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0 
        else:
            return n
        
def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número real válido.\033[m")
            continue
        except (KeyboardInterrupt, SystemExit):
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0 
        else:
            return n
    
num = leia_int("Digite um valor: ")
num2 = leia_float("Digite outro valor: ")
print(f"\033[32mO valor inteiro digitado foi {num} e o valor real digitado foi {num2}\033[m")