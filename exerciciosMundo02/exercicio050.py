soma = 0
cont = 0
for x in range (1,7):
    y = int(input('Digite o {}o número: '.format(x)))
    if y%2==0:
        soma += y
        cont += 1
print('A soma dos {} valores pares foi: {}'.format(cont, soma))
