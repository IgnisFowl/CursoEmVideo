'''x = [2, 5, 4, 3]
print(x)
x[2] = 5
print(x)
x.append(7)
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)
print(f'Essa lista tem {len(x)} elementos.')
x.insert(2,2)
print(x)
x.pop()
print(x)
x.pop(2)
print(x)
x.remove(5) #remove apenas o primeiro elemento encontrado
print(x)
if 5 in x:
    x.remove(5)
else:
    print('Não achei o número 5.')
print(x)'''

'''valores = []
for cont in range(0,5):
    valores.append(int(input('Digite o valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}...')
print('fim')'''

a = [1, 2, 3, 4]
b = a[:]
b[2] = 8
print(a)
print(b)
