x = int(input('Digite o primeiro termo da P.A.: '))
y = int(input('Digite a razão da P.A.: '))
total = 0
mais = 10
c = 1
while mais != 0:
    total += mais
    while c <= total:
        z = x + c * y
        c += 1
        print(z, end=' ')
    print('\nPAUSA')
    mais = int(input('\nVocê gostaria de ver mais quantos termos da P.A.? '))
print('Progressão finalizada com {} termos.'.format(total))
print('FIM')
