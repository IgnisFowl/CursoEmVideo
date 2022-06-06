'''help(print)
print()
print(input.__doc__)'''
'''from time import sleep
def contador(i,f,p):
    """
    Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    c=i
    while c<=f:
        print(f'{c}', end='..')
        c += p
        sleep(0.5)
    print('fim')

contador(2,10,2)

help(contador)'''

'''def somar(a=0,b=0,c=0):
    #se não receber c, ele recebe zero: parâmetro opcional.
    s=a+b+c
    print(f'A soma vale {s}.')


somar(3,2,5)
somar(8,4)
somar(c=3, b=2)
somar()'''


'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


s1 = somar(3, 2, 5)
s2 = somar(2, 4)
print(f'A soma 1 vale {s1}, e a 2 vale {s2}.')'''

'''def fatorial(num = 1):
    f = 1
    for c in range (num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')'''

def parouimpar(n=0):
    if n%2==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if parouimpar(num):
    print('é par')
else:
    print('é ímpar')