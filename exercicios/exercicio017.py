'''import math
l1 = float(input('Digite o cateto oposto: '))
l2 = float(input('Digite o cateto adjacente: '))
l3 = (l1**2)+(l2**2)
print('A hipotenusa é: {}'.format(math.sqrt(l3)))'''

from math import hypot
l1 = float(input('Digite o cateto oposto: '))
l2 = float(input('Digite o cateto adjacente: '))
l3 = hypot(l1,l2)
print('A hipotenusa é: {:.2f}'.format(l3))