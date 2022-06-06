'''n = input('Digite um numero: ')
print('Milhar: ',n[0])
print('Centena: ',n[1])
print('Dezena: ',n[2])
print('Unidade: ',n[3])'''

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Milhar: ',m)
print('Centena: ',c)
print('Dezena: ',d)
print('Unidade: ',u)