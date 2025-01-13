# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

def area(largura, comprimento) -> float:
    area = largura * comprimento
    return f"A área de um terreno {largura}x{comprimento} é de {area}m²"

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

print(area(largura, comprimento))