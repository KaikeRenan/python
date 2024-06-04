# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v_carro = int(input('Qual a velocidade atual do carro? '))

# if v_carro > 80:
#     print('MULTADO! voce execedeu o limite permitido que é de 80km/h')
#     multa = (v_carro-80)*7
#     print('Voce deve pagar uma multa de R${multa:.2f}!')
# print('Tenha um bom dia! Dirija com segurança!')

if v_carro <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else: 
    excesso = v_carro - 80 
    multa = excesso*7
    print(f"""MULTADO! voce execedeu o limite permitido que é de 80km/h
Voce deve pagar uma multa de R${multa:.2f}!
Tenha um bom dia! Dirija com segurança!""")
    
    