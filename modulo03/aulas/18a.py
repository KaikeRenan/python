# dados1 = []
# dados2 = []
# dados3 = []

# dados1.append('Pedro')
# dados1.append(25)
# dados2.append('Maria')
# dados2.append(19)
# dados3.append('João')
# dados3.append(32)

# pessoas = []

# pessoas.append(dados1[:])
# pessoas.append(dados2[:])
# pessoas.append(dados3[:])

# print(pessoas)

#--------------------------------------------------------------------

pessoas = [['Pedro',25],['Maria',19],['João',32]]

print(pessoas[0][0])

print(pessoas[1][1])

print(pessoas[2][0])

print(pessoas[1])

#--------------------------------------------------------------------

# pessoas = [['João',19], ['Ana',33], ['Joaquim',13], ['Maria', 45]]

# for pessoa in pessoas:
#     print(pessoa)

# print('\n')

# for pessoa in pessoas:
#     print(pessoa[0])

# print('\n')

# for pessoa in pessoas:
#     print(pessoa[1])

# print('\n')

# for pessoa in pessoas:
#     print(f"{pessoa[0]} tem {pessoa[1]} anos")

#--------------------------------------------------------------------

# pessoas = []

# dados = []

# qt_maior = qt_menor = 0

# for c in range(0,3):
#     dados.append(str(input("Nome: ")))
#     dados.append(int(input("Idade: ")))
    
#     pessoas.append(dados[:])
    
#     dados.clear()
    
# # print(pessoas)

# for pessoa in pessoas:
#     if pessoa[1] >= 18:
#         print(f"{pessoa[0]} é maior de idade")
#         qt_maior += 1
#     else:
#         print(f"{pessoa[0]} é menor de idade")
#         qt_menor += 1
        
# print(f"Temos {qt_maior} {'maior' if qt_maior == 1 else 'maiores'} de idade e {qt_menor} {'menor' if qt_menor == 1 else 'menores'} de idade")