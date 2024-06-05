nome = str(input('Qual é seu nome? '))

#estrutura condicional aninhada (formato de ninho - um dentro do outro)

if nome == 'Kaike':
    print('Que nome bonito')
elif nome == 'Pedro' or nome =='Maria' or nome == 'Paulo':
    print('Seu nome é comum no Brasil')
elif nome in 'Beatriz':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
    
print(f'Tenha um bom dia, {nome}')