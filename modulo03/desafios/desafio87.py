# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.                
# B) A soma dos valores da terceira coluna.                  
# C) O maior valor da segunda linha

matriz = [[0,0,0], [0,0,0], [0,0,0]]

soma_pares = soma_terceira = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l}, {c}]: "))

print('\n')

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
    
print('\n')
    
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
print(f"Soma dos pares digitados: {soma_pares}")

for l in range(0, 3):
    soma_terceira += matriz[l][2] 
print(f"Soma dos valores da terceira coluna: {soma_terceira}")

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c] 
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c] 
            
print(f"O maior valor da segunda linha: {maior}")