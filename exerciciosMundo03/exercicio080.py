v = []
for c in range(0, 5):
    x = int(input('Digite um valor: '))
    if c == 0 or x > v[-1]:
        v.append(x)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(v):
            if x < v[pos]:
                v.insert(pos, x)
                print(f'Valor adicionado na posição {pos} da lista.')
                break
            pos +=1
print(f'Os valores digitados, em ordem, foram {v}.')


