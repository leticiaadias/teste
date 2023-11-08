#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
#Depois mostre:
#A) Os 5 primeiros.
#B) Os últimos 4 colocados.
#C) Times em ordem alfabética.
#D) Em que posição está o time da chapecoense.

brasileirao=('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
print('-='*20)
print(f'Tabela do brasileirão 2018: {brasileirao}')
print('-='*20)
print(f'Os 5 primeiros colocados do brasileirão são {brasileirao[0:5]}')
print('-='*20)
print(f'Os últimos quatro colocados do brasileirão são {brasileirao[16:]}') #ou [-4:]
print('-='*20)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(f'O time Chapecoense esta na posição {brasileirao.index("Chapecoense")+1}ª')
