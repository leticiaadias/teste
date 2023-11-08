#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso serpa guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


fut=dict()
partidas=list()
fut['nome']=str(input('Nome do Jogador: '))
tot=int(input(f'    Quantas partidas {fut["nome"]} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos Gols na partida {c+1}? ')))
fut['gols']=partidas
fut['total']=sum(partidas)
print(fut)
print('-='*25)
for k, v in fut.items():
    print(f'O campo {k} tem valor {v}')
print('-='*25)
print(f'O jogador {fut["nome"]} jogou {len(partidas)} partidas.')
for i, v in enumerate(fut["gols"]):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {fut["total"]} gols.')
