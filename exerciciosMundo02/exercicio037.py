x = int(input('Digite um número inteiro: '))
y = int(input('Escolha a base de conversão: \n 1 para binario \n 2 para octal \n 3 para hexadecimal \n Digite a opção desejada:  '))
if y == 1:
    b = bin(x)
    print('{} em binário é: {}'.format(x, b[2:]))
elif y == 2:
    o = oct(x)
    print('{} em octal é: {}.'.format(x, o[2:]))
elif y == 3:
    h = hex(x)
    print('{} em hexadecimal é: {}.'.format(x, h[2:]))
else:
    print('Opção inválida.')
