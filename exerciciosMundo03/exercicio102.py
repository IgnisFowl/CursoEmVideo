def fatorial(num = 1, y=False):
    """
    Calcula o fatorial de um número:
    :param num: numero a ser calculado.
    :param y: (opcional) mostrar ou não a conta.
    :return: o fatorial do numero.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if y:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print(f' = {f}.')
        else:
            if c == 1:
                print(f)
    return f


#x = int(input('Digite um número: '))
#y = bool(input('Deseja ver o processo do fatorial [True/False]? '))
fatorial(5, True)
help(fatorial)
