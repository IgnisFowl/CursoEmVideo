partidas = []
jogador = {}
tot = 0
jogador["nome"] = str(input('Nome do jogador: '))
x = int(input('No de partidas: '))
for r in range(1, x+1):
    partidas.append(int(input(f'No de gols na partida {r}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('~*'*10)
print(jogador)
print('~*'*10)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('~*'*10)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas e fez {jogador["total"]} gols no total.')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')