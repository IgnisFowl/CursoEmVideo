matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = c3 = m2l = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] %2==0:
            pares += matriz[l][c]
    if matriz[1][c] > m2l:
        m2l = matriz[1][c]
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos números pares foi: {pares}.')
#c3 = matriz[0][2]+matriz[1][2]+matriz[2][2]
for l in range(0,3):
    c3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna foi: {c3}.')
print(f'O maior valor da segunda linha é: {m2l}.')


