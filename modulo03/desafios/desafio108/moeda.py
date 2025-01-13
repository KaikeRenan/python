def aumentar(n = 0, aumento = 0):
    n *= 1 + (aumento/100)
    return n
    
def diminuir(n = 0, desconto = 0):
    n *= 1 - (desconto/100)
    return n
    
def dobro(n = 0):
    return 2*n
    
def metade(n = 0):
    return n/2

def moeda(n = 0, moeda = 'R$'):
    return f"{moeda}{n:.2f}".replace('.',',')