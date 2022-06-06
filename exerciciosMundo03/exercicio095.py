partidas = []
jogador = {}
lista = []
tot = 0
while True:
    jogador["nome"] = str(input('Nome do jogador: '))
    x = int(input('No de partidas: '))
    partidas.clear()
    for r in range(1, x+1):
        partidas.append(int(input(f'    No de gols na partida {r}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista.append(jogador.copy())
    while True:
        r = str(input('Deseja continuar [s/n]: ')).strip().lower()[0]
        if r not in "SsNn":
            print('Erro! Digite apenas S ou N.')
        else:
            break
    if r == 'n':
        break
print('~*'*15)
print(lista)
print('~*'*15)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para): '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'Erro! Não existe jogador com código {busca}.')
    else:
        print('-' * 40)
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}:')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('VOLTE SEMPRE')