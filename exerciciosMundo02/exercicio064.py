x = soma = cont = 0
x = int(input('Digite um número: '))
while x != 999:
    x = int(input('Digite um número: '))
    if x != 999:
        soma += x
    cont += 1
print('A soma dos {} números digitados foi: {}'.format(cont, soma))
print('FIM')
