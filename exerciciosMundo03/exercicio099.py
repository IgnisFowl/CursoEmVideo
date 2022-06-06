def maior(*x):
    c = maior = 0
    print('Analisando os valores passados...')
    for n in x:
        print(f'{n} ', end='')
        if c == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        c += 1
    print(f'Foram informados {c} valores. O maior valor foi {maior}.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()