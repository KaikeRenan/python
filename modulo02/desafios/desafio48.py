# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
valores = 0

# for c in range(1,501,2):
for c in range(1,501):
    if (c % 2 == 1) and (c % 3 == 0):
        soma += c # soma = soma + c
        valores += 1 # valores = valores + 1
        
print(f"A soma de todos os {valores} valores solicitados é {soma}")
