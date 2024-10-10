# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. 

primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

termo = primeiro 
contador = 1

total = 0
escolha = 10

while escolha != 0:
    total = total + escolha
    while contador <= total:
        print(f"{termo} -> ", end='')
        termo += razao
        contador += 1
    print("PAUSA")
    escolha = int(input("\nQuantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos utilizados")