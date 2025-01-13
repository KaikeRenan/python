def aumentar(n, aumento):
    n *= 1 + (aumento/100)
    return n
    
def diminuir(n, desconto):
    n *= 1 - (desconto/100)
    return n
    
def dobro(n):
    return 2*n
    
def metade(n):
    return n/2