nome = input('Qual e seu nome? ')
print('Prazer em te conhecer {:~^20}!'.format(nome))
n1 = int(input('Digite um valor: '))
n2 =  int(input('Digite outro valor: '))
s = n1 + n2
d = n1 / n2
m = n1 * n2
sb = n1 - n2
di = n1 // n2
ex = n1 ** n2
print('Soma: {}, divisão: {:.3f}, produto: {}, \n subtração: {},'
      ' divisão inteira: {}, exponenciação: {}'.format(s,d,m,sb,di,ex))
