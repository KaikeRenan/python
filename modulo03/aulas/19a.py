# # dados = dict()

# dados = {'nome':'Pedro','idade':25}

# print(dados['nome'])
# print(dados['idade'])

# dados['sexo'] = 'M' #cria o elemento sexo e coloca M dentro

# del dados['idade'] #deleta idade

#--------------------------------------------------------------------

# filme = {
#     'titulo':'Star Wars',
#     'ano': 1977,
#     'diretor': 'George Lucas'
# }

# # print(filme.values())

# # print(filme.keys())

# # print(filme.items())

# for keys, values in filme.items():
#     print(f"O {keys} é {values}")
    
#--------------------------------------------------------------------
    
# locadora = [{'titulo':'Star Wars','ano': 1977,'diretor': 'George Lucas'}, {'titulo':'Avengers','ano': 2012,'diretor': 'Joss Whedon'}, {'titulo':'Matrix','ano': 1999,'diretor': 'Wachowski'}]

# print(locadora[0]['ano'])
# print(locadora[2]['titulo'])

#--------------------------------------------------------------------

# pessoas = {'nome': 'Kaike', 'sexo': 'M', 'idade': 18}

# print(pessoas)
# print(pessoas['nome'])
# print(pessoas['idade'])
# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for key in pessoas.keys():
#     print(key)

# for value in pessoas.values():
#     print(value)

# for item in pessoas.items():
#     print(item)

# del pessoas['sexo']

# pessoas['nome'] = 'Renan' 

# pessoas['peso'] = 56.40

# for keys, values in pessoas.items():
#     print(f"{keys} = {values}")

#--------------------------------------------------------------------

# brasil = []

# estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf':'São Paulo', 'sigla': 'SP'}

# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])

#--------------------------------------------------------------------

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # brasil.append(estado[:]) #não pode o fatiamento
    brasil.append(estado.copy()) 

for e in brasil:
    # for k, v in e.items():
    #     print(f"O campo {k} tem valor {v}")
    for v in e.values():
        print(v,end=' ')
    print()