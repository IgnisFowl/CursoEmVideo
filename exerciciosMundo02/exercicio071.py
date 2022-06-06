#x = int(input('Digite o valor a ser sacado: R$'))
#notas50 = x // 50
#resto1 = x - notas50*50
#notas20 = resto1 // 20
#resto2 = resto1 - notas20*20
#notas10 = resto2 // 10
#resto3 = resto2 - notas10*10
#notas1 = resto3 // 1
#print(f'''{notas50} notas de R$50
#{notas20} notas de R$20
#{notas10} notas de R$10
#{notas1} notas de R$1''')

print('='*50)
print('{:^50}'.format('BANCO GUANABARA'))
print('='*50)
x = int(input('Digite o valor a ser sacado: R$'))
total = x
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('='*50)
print('{:^50}'.format('VOLTE SEMPRE!'))
print('='*50)