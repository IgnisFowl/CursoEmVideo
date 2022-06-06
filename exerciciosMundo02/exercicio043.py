p = float(input('Digite o peso da pessoa, em kg: '))
a = float(input('Digite a altura da pessoa, em m: '))
imc = p / (a*a)
print('Seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('A pessoa está abaixo do peso.')
elif imc < 25:
    print('A pessoa está no peso ideal.')
elif imc < 30:
    print('A pessoa está no sobrepeso.')
elif imc < 40:
    print('A pessoa está obesa.')
else:
    print('A pessoa está com obesidade mórbida.')