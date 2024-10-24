# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

tabela_2024 = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Internacional', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Vasco da Gama', 'Grêmio', 'Criciúma', 'Bragantino', 'Juventude', 'Athletico-PR', 'Fluminense', 'EC Vitória', 'Corinthians', 'Cuiabá', 'Atlético-GO',)

print(f"Lista de times  do Brasileirão: {tabela_2024}")
print('\n')
print(f"Os 5 primeiros são {tabela_2024[:5]}")
print('\n')
print(f"Os 4 últimos são {tabela_2024[-4:]} ")
print('\n')
print(f"Times em ordem alfabética: {sorted(tabela_2024)}")
print('\n')
print(f"A Chapecoense está na {tabela_2024.index("Vasco da Gama")+1}° posição")