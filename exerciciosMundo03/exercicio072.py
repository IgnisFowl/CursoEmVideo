tupla = ('zero','um','dois','três','quatro','cinco','seis',
         'sete','oito','nove','dez','onze','doze','treze',
         'catorze','quinze','dezesseis','dezessete','dezoito',
         'dezenove','vinte')
while True:
    x = int(input('Digite um número entre 0 e 20: '))
    if x < 0 or x > 20:
        print('Tente novamente.')
        x = int(input('Digite um número entre 0 e 20: '))
    else:
        print('Você digitou o número {}.'.format(tupla[x]))
    y = str(input('Você deseja continuar [s/n]? ')).strip().lower()[0]
    if y == 'n':
        break
print('fim')