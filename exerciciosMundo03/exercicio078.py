valores = []
menor = maior = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite o {cont}o valor: ', )))
print(f'O maior valor foi {max(valores)} na posição: ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}')
print(f'O menor valor foi {min(valores)} na posição: ', end='')
for j, w in enumerate(valores):
    if w == min(valores):
        print(f'{j} ', end='...')
