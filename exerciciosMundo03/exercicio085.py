lista = [[],[]]
for c in range(0,7):
    x = int(input('Digite um valor: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
lista[0].sort()
lista[1].sort()
print(lista)
print(f'Os números pares são: {lista[0]}.')
print(f'Os números ímpares são: {lista[1]}.')