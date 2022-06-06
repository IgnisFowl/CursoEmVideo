n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('Sua média foi {:.2f}, e você está REPROVADO!'.format(m))
elif m >= 5 and m <= 6.9:
    print('Sua média foi {:.2f}, e você está de RECUPERAÇÃO!'.format(m))
else:
    print('Sua média foi {:.2f}, e você está APROVADO! Parabéns!'.format(m))
