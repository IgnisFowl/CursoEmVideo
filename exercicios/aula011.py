
'''print('\033[0;30;47mHello World!\033[m')
print('\033[1;31;46mHello World!\033[m')
print('\033[4;32;45mHello World!\033[m')
print('\033[7;30;44mHello World!\033[m')
print('\033[4;30;42mHello World!')
print('\033[m')
nome = 'Guanabara'
print('Hello World, {}{}{}!'.format('\033[4;30;42m', nome, '\033[m'))'''

nome = 'Aline'
cores = { 'limpo':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpo']))