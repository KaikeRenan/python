def aumentar(n = 0, aumento = 0, formato=False):
    res = n + (n * aumento / 100)
    return res if formato is False else moeda(res)
    
def diminuir(n = 0, desconto = 0, formato=False):
    res = n - (n * desconto / 100)
    return res if formato is False else moeda(res)
    
def dobro(n = 0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)
    
def metade(n = 0, formato=False):
    res = n/2
    return res if not formato else moeda(res)

def moeda(n = 0, moeda = 'R$'):
    return f"{moeda}{n:.2f}".replace('.',',')