x = []
y = []
maior = menor = 0
while True:
    x.append(str(input('Nome: ')))
    x.append(int(input('Peso: ')))
    if len(y) == 0:
        maior = menor = x[1]
    else:
        if x[1] > maior:
            maior = x[1]
        if x[1] < menor:
            menor = x[1]
    y.append(x[:])
    r = str(input('Deseja adicionar outra pessoa [s/n]?')).strip().lower()
    if r == 'n':
        break
    x.clear()

print(f'Ao todo você cadastrou {len(y)} pessoas.')
print(f'O maior peso foi: {maior}, das pessoas: ', end='')
for p in y:
    if p[1] == maior:
        print(f'{p[0]}', end='...')
print(f'\nO menor peso foi: {menor}, das pessoas: ', end='')
for q in y:
    if q[1] == menor:
        print(f'{q[0]}', end='...')


