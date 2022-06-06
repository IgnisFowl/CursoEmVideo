x = int(input('Digite o primeiro lado do triangulo: '))
y = int(input('Digite o segundo lado do triangulo: '))
z = int(input('Digite o terceiro lado do triangulo: '))
if (x < y + z) and (y < z + x) and (z < x + y):
    print('É um triângulo!')
else:
    print('Não pode ser um triângulo!')