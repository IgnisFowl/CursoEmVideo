x = float(input('Digite o primeiro lado do triângulo: '))
y = float(input('Digite o segundo lado do triângulo: '))
z = float(input('Digite o terceiro lado do triângulo: '))
if (x < y + z) and (y < x + z) and (z < x + y):
    print('Pode sim formar um triângulo: ', end='')
    if x == y == z:
        print('equilátero!')
    elif x == y or y == x or y == z:
        print('isósceles!')
    else:
        print('escaleno!')
else:
    print('Não pode formar um triângulo!')
