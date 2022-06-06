c = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
if 9 in c:
    print(f'Quantas vezes apareceu o número 9: {c.count(9)+1} vezes.')
else:
    print('O valor 9 não foi digitado.')
if 3 in c:
    print(f'Em que posição foi digitado o primeiro valor 3: {c.index(3)}.')
else:
    print('O valor 3 não foi digitado.')
print('Os números pares foram: ', end='')
for x in c:
    if x % 2 == 0:
        print(x, end=' ')
