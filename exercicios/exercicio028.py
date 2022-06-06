import random
from time import sleep
n = random.randrange(0,5,1)
x = (input('Adivinhe o número de 0 a 5: '))
print('PROCESSANDO')
sleep(3)
print('O número sorteado foi {}!'.format(n))
print('Parabéns, você acertou!'if x==n else 'Você errou!' )

