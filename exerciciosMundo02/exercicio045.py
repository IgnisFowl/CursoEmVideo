from random import choice
from time import sleep
print('JOKENPO!')
y = str(input('pedra, papel ou tesoura? \n')).lower()
lista = ['pedra','papel','tesoura']
x = choice(lista)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('Você jogou: {}.'.format(y))
print('O computador jogou: {}'.format(x))
if x == y:
    print('Empate!')
elif y == 'papel' and x == 'pedra':
    print('Você ganhou!')
elif y == 'pedra' and x == 'papel':
    print('Você perdeu!')
elif y == 'tesoura' and x == 'papel':
    print('Você ganhou!')
elif y == 'papel' and x == 'tesoura':
    print('Você perdeu!')
elif y == 'tesoura' and x == 'pedra':
    print('Você perdeu!')
else:
    print('Jogada inválida!')

