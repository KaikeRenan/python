# Interactive Help

help(print)

print(input.__doc__)

# Docstrings

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.

    Args:
        i (int): início da contagem
        f (int): fim da contagem
        p (int): passo da contagem
        return: sem retorno
    """
    c = 1
    while c <= f:
        print(f"{c}", end='')
        c += p
    print("FIM!\n")
    
help(contador)

# Parâmetros Opcionais

def somar(a=0, b=0, c=0,):
    soma = a+b+c
    print(f"A soma vale {soma}\n")

somar(5, 10)

# Escopo de variáveis

def teste(b):
    global a # não crie uma variável local e use a variável global
    a = 8 # variáveis locais
    b += 4 # variáveis locais
    c = 2 # variáveis locais
    print(f"A dentro de teste {a}")
    print(f"B dentro de teste {b}")
    print(f"C dentro de teste {c}")
    
a = 5 # variável global
teste(a)
print(f"A fora vale {a}\n")

# Retorno de valores

def somar(a=0, b=0, c=0,):
    soma = a+b+c
    return soma

resp1 = somar(3, 2, 5)
# print(somar(3, 2, 5))

resp2 = somar(1, 7)
resp3 = somar(4)

print(f"Meus cálculos deram {resp1}, {resp2} e {resp3}.\n")

# exercício

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

# n = int(input("Digite um número: "))
# print(f"O fatorial de {n} é igual a {fatorial(n)}")

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são {f1}, {f2} e {f3}\n")

def par_ou_impar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Digite um número: "))
if(par_ou_impar(num)):
    print("Par")
else:
    print("Ímpar")