'''x = int(input('Digite um número: '))
if x == 2 or x == 3 or x == 5 or x == 7:
    print('É um número primo!')
elif x%2==0 or x%3==0 or x%5==0 or x%7==0:
    print('Não é um número primo!')
else:
    print('É um número primo!')'''

tot = 0
x = int(input('Digite um número: '))
for c in range (1, x+1):
    if x % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='' )
print('\n\033[m O número {} foi divisível {} vezes.'.format(x, tot))
if tot > 2:
    print('O número \033[31mnão é primo.')
else:
    print('O número é \033[34mprimo.')