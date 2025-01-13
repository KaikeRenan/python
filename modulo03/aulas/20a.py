# print("-"*30)
# print("    Sistema de Alunos")
# print("-"*30)
# print("    Cadastro de funcionários")
# print("-"*30)
# print("    Erro do sistema")
# print("-"*30)

# mesmo código usando funções
# def mostrar_linha():
#     print("-"*30)   
    
# mostrar_linha()
# print("    Sistema de Alunos")
# mostrar_linha()
# print("    Cadastro de funcionários")
# mostrar_linha()
# print("    Erro do sistema")
# mostrar_linha()

#função com parâmetro
# def mensagem(msg):
#     print("-"*30)
#     print(msg)
#     print("-"*30)
    
# mensagem('Sistema de Alunos')

# def calcular_soma(num1, num2):
#     print(num1 + num2)
    
# calcular_soma(num1=4, num=25)
# calcular_soma(num2=8, num1=9)
# calcular_soma(2, 1)

# desempacota
# def contador(*num): #*num desempacota tupla
#     # print(num)
    
#     # for valor in num:
#     #     print(f"{valor} ",end="")
#     # print('Fim')
    
#     tamanho = len(num)
#     print(f"Recebi os valores {num} e são ao todo {tamanho} números")
    
# contador(5, 7, 3, 1, 4)
# contador(8, 7, 1)

# desempacota
# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f"Somando os valores {valores} temos {s}")
    
# soma(5,2)
# soma(2,9,4)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
