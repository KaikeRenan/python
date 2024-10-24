# lanche = ['lanche', 'suco', 'pizza', 'pudim']

# print(lanche)

# lanche[3] = 'picolé' #adiciona o tem picolé no índice 3

# print(lanche)

# lanche.append('biscoito') #adiciona um índice no final da lista

# print(lanche)

# lanche.insert(0,'cachorro quente') #adiciona no índice que eu quiser da lista

# print(lanche)

# del(lanche) #deleta a lista inteira
# del lanche[3] #deleta somente o índice 3

# lanche.pop() #deleta o ultimo índice
# lanche.pop(3) #deleta somente o índice 3

# lanche.remove('pizza') #deleta o índice pelo nome do item

# print(lanche) 

#verificação se o item está na lista
# if 'pizza' in lanche:
#     lanche.remove('pizza') 

#--------------------------------------------------------------------

# valores = list(range(4,11)) #função list(para criar listas)

# print(valores)

#--------------------------------------------------------------------

# valores = [8,2,5,4,9,3,0]

# print(valores)

# valores.sort() #organiza a lista de forma crescente

# print(valores)

# valores.sort(reverse=True) #organiza a lista de forma decrescente

# print(valores)

# print(len(valores)) #conta a quantidade de elementos

#--------------------------------------------------------------------

# num = [2,5,9,1]

# num[2] = 3

# num.append(7)

# # num.sort()
# num.sort(reverse=True)

# # num.insert(2, 0)
# num.insert(2,2)

# # num.pop()
# num.pop(2)

# # num.remove(2)
# if 4 in num:
#     num.remove(4)
# else:
#     print('não encontrei o número 4 na lista')

# print(num)

# print(len(num))

#--------------------------------------------------------------------

# valores = list()
# valores = []

# # valores.append(5)
# # valores.append(9)
# # valores.append(4)

# for cont in range(0,5):
#     valores.append(int(input("Digite um valor: ")))

# for indice, valor in enumerate(valores):
#     print(f"Na posição {indice} encontrei o valor {valor}!")
# print("Cheguei ao final da lista!!!")

#--------------------------------------------------------------------

a = [2,3,4,7]

# b = a #ligação entre as duas listas

b = a[:] #recebe todos os valores de a

b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")
