salario = float(input('Digite seu salário para saber o seu aumento: '))
if salario >=1250:
    aumento = salario + (salario/100)*10
    print('Seu salário agora é: {}.'.format(aumento))
else:
    aumento2 = salario + (salario/100)*15
    print('Seu salário agora é: {}.'.format(aumento2))
