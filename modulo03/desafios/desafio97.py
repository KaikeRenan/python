# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~                                                                                                                                                            
# Olá, Mundo!                                                                                                                                                         
# ~~~~~~~~~    

def escreva(texto):
    tamanho = len(texto) + 4
    linha = '~'*tamanho
    return f"{linha}\n{texto}\n{linha}"

print(escreva(input("Digite uma frase: ")))
