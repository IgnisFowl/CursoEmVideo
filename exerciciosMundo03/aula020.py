'''def mensagem(msg):
    print('~*'*30)
    print(f'{msg:^60}')
    print('~*'*30)


mensagem('SISTEMA DE ALUNOS')'''

'''def soma(x, y):
    print(x-y)


soma(y=4, x=5)
soma(8, 9)'''

'''def contador(*x):
    for v in x:
        print(v, end=' ')
    print(f'Recebi {len(x)} valores.')
    print()


contador(2, 1, 7)
contador(8, 0)
contador(4, 5, 7, 3)'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é {s}.')


soma(5, 2)
soma(3, 4, 11)



