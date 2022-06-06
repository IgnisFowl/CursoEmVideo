teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

pessoas = [['João', 19], ['Maria', 15], ['Ana', 14], ['Beto',12]]
print(pessoas[0][0])
print(pessoas[1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos.' )

x = list()
y = list()
for c in range(0,3):
    y.append(str(input('Nome: ')))
    y. append(int(input('Idade: ')))
    x.append(y[:])
    y.clear()
print(x)
print(y)

for p in x:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')