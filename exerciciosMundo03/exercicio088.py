from random import randint
from time import sleep
tot = 1
lista = []
jogos = []
vezes = int(input('Quantos jogos deseja sortear? '))
while tot <= vezes:
    cont = 0
    while True:
        x = randint(1,60)
        if x not in lista:
            lista.append(x)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-~'*5, f'SORTEANDO {vezes} JOGOS ', '-~'*5)
for c in range(0,len(jogos)):
    print(f'{c+1}o jogo: {jogos[c]}')
    sleep(1)