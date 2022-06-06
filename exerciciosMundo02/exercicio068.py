from random import randint
cont = n = 0
while True:
    p = ' '
    while p not in 'PpIi':
        p = str(input('Par ou Ímpar? ')).strip().lower()[0]
    n = int(input('Escolha um número de 0 a 10: '))
    c = randint(0,10)
    s = c + n
    if s%2==0 and p == 'p':
        print(f'Você jogou {n} e o computador jogou {c}.')
        print('Você venceu!')
        cont += 1
    elif s%2!=0 and p == 'i':
        print(f'Você jogou {n} e o computador jogou {c}.')
        print('Você venceu!')
        cont += 1
    else:
        print(f'Você jogou {n} e o computador jogou {c}.')
        print('Você perdeu!')
        break
    print('Vamos jogar novamente...')
if cont > 0:
    print(f'Você teve {cont} vitória(s) consecutiva(s)!')
else:
    print('FIM')