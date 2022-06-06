from random import randint
from time import sleep


def sorteio(lista):
    for i in range(0,5):
        x = randint(1,100)
        lista.append(x)
        print(f'{x} ', end='')
        sleep(0.5)
    print()



def somapar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é {soma}.')

numeros=list()
sorteio(numeros)
somapar(numeros)

print(numeros)