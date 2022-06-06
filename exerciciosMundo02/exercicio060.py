'''x = int(input('Digite um número: '))
y = 1
if x >= 1:
    for i in range (1, x+1):
        y = y * i
print('Fatorial de {} é {}.'.format(x, y))'''

'''from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

x = int(input('Digite um numero: '))
c = x
f = 1
print('Calculando fatorial de {}! '.format(x))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print(f)


