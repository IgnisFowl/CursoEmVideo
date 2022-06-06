lanche = ('hamburguer', 'sorvete', 'pizza', 'pudim')
print(lanche[0:2], len(lanche))
#lanche[2] = 'sorvete'
#tuplas são imutáveis
for comida in lanche:
    print(f'Eu vou comer {comida}!')

for c in range (0, len(lanche)):
    print(lanche[c])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
print(sorted(lanche))

a = (1, 2, 3)
b = (4, 5, 6, 7, 3)
c = b + a
print(a)
print(b)
print(c)
print(sorted(c))
print(c.count(5)) #quantas vezes aparece 5 na tupla c
print(c.index(3)) #em que posição está o 3 na tupla c
print(c.index(3,5)) #deslocamento
del(b)
print(b)
