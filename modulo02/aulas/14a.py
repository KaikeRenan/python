# c = 1

# while c <= 10:
#     print(c)
#     c += 1
# print("Acabou")

#--------------------------------------------------------------------

# n = 1

# while n != 0: #condição de parada (flag)
#     n = int(input("Digite um valor: "))
# print("Acabou")

#--------------------------------------------------------------------

# r = 'S'

# while r == 'S':
#     r = int(input("Digite um valor: "))
#     r = str(input("Quer continuar? [S/N]: ")).upper()
# print("Fim")

#--------------------------------------------------------------------

n = 1
par = impar = 0

while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números ímpares!")
