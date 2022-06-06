'''nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
nome2 = nome.split()
nome3 = ''.join(nome2)
print(len(nome3))
print(len(nome2[0]))'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
