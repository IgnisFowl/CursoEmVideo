'''tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo <=3 else 'carro velho')
print('fim')'''

'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem.')
else:
    print('Seu nome é feio.')
print('Bom dia, {}.'.format(nome))'''


'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.2f}.'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Você está de recuperação.')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.2f}.'.format(m))
print('PARABÉNS' if m>=6 else 'ESTUDE MAIS!')
