a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))
'''if a<b and a<c:'''
menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
'''if a>b and a>c:'''
maior = a
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c
print('O menor número foi {} e o maior foi {}.'.format(menor,maior))


