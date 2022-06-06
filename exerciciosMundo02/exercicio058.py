'''import random
from time import sleep
n = random.randrange(0,5,1)
x = int(input('Adivinhe o número de 0 a 5: '))
while x != n:
    print('Número errado, tente novamente!')
    x = int(input('Adivinhe o número de 0 a 5: '))
print('PROCESSANDO')
sleep(3)
print('O número sorteado foi {}!'.format(n))
print('Parabéns, você acertou!'if x==n else 'Você errou!' )'''

from random import randint
from time import sleep
n = randint(0,10)
print('O computador acabou de pensar em um número de 0 a 10!')
acertou = False
c = 0
while not acertou:
    x = int(input('Adivinhe o número: '))
    c += 1
    if x == n:
        acertou = True
    elif x > n:
        print('Tente um número menor!')
    elif x < n:
        print('Tente um número maior!')

print('PARABENS! Acertou em {} tentativas!'.format(c))
