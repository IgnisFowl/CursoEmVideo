from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f}, de {p} em {p}:')
    if f > i:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
            sleep(0.5)
    else:
        cont2 = i
        while cont2 >= f:
            print(f'{cont2} ', end='', flush=True)
            cont2 -= p
            sleep(0.5)
    print('fim')


contador(1,10,1)
contador(10,0,2)
print('Contador personalizado:')
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)
