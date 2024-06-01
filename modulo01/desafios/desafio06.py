# crie um código que leia um número e mostre o seu dobro, tripo e raiz quadrada

num = int(input('Digite um número: '))

dobro = num*2
triplo = num*3
raiz_quadrada = num**(1/2)

print(f'Número escolhido: {num}\nSeu dobro: {dobro}\nSeu triplo: {triplo}\nSua raiz quadrada: {raiz_quadrada:.0f}')