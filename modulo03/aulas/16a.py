# lanche = ('Hambúrger','Suco', 'Pizza','Pudim','Batata Frita') #TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'Refrigerante' - Erro

# print(lanche)

# print(sorted(lanche)) #coloca em ordem

# for comida in enumerate(lanche):
#     print(f'Eu vou comer {comida}')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} e a sua posição é {cont}')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} e a sua posição é {pos}')

#Fatiamento
# print(lanche[2])

# print(lanche[-2])

# print(lanche[1:3])

# print(lanche[2:])

# print(lanche[:2])

# lanche = 'Hambúrger','Suco', 'Pizza','Pudim'
# print(lanche)

# print(len(lanche))

#--------------------------------------------------------------------

# a = (2,5,4)
# b = (5,8,1,2)
# c = a+b #junta
# # c = b+a #ordem importa

# print(c)
# print(len(c))
# print(c.count(5)) #conta quantas vezes aparece o elemento na tupla
# print(c.index(5, 2)) #qual a posição do elemento, apartir de tal posição

#--------------------------------------------------------------------

pessoa = ('Gustavo',39,'M',99.88) #aceita outros tipos
# del(pessoa) #apaga da memória, uníca coisa q pode ser feita depois definir uma tupla
print(pessoa)