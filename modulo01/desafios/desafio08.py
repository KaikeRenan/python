# crie um código que leia um valor em metros e o exiva convertido em centímetros e milímetros

num = float(input('Digite uma medida em metros: '))

print(f'Convertendo para centímetro: {num*100:.0f}\nConvertendo para milímetros: {num*1000:.0f}')