from time import sleep
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
z = 0
while z != 5:
    sleep(2)
    print('''Digite a opção desejada: 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    z = int(input(''))
    if z == 1:
        print('A soma dos dois valores é {}.'.format(x+y))
        print('-'*10)
    elif z == 2:
        print('O produto dos dois valores é {}.'.format(x*y))
        print('-' * 10)
    elif z == 3:
        if x > y:
            print('O maior valor é {}.'.format(x))
            print('-' * 10)
        else:
            print('O maior valor é {}.'.format(y))
            print('-' * 10)
    elif z == 4:
        print('Digite novamente os valores!')
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))
        print('''Digite a opção desejada: 
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        ''')
        z = int(input(''))
        if z == 1:
            print('A soma dos dois valores é {}.'.format(x + y))
            print('-' * 10)
        elif z == 2:
            print('O produto dos dois valores é {}.'.format(x * y))
            print('-' * 10)
        elif z == 3:
            if x > y:
                print('O maior valor é {}.'.format(x))
                print('-' * 10)
            else:
                print('O maior valor é {}.'.format(y))
                print('-' * 10)
    else:
        print('Opção Inválida!')
        print('-' * 10)
print('FIM')
