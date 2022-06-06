maior = 0
menor = 0
for c in range (1,6):
    peso = int(input('Digite o peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso foi {} e o menor foi {}'.format(maior, menor))
