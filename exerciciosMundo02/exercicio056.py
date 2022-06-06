maisvelho = 0
omaisvelho = ''
menos20 = 0
soma = 0
for c in range (1,5):
    print('-------- {}a PESSOA --------'.format(c))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo: feminino ou masculino? ')).strip().lower()
    soma += idade
    if sexo == 'masculino' and idade > maisvelho:
        maisvelho = idade
        omaisvelho = nome
    elif sexo == 'feminino' and idade < 20:
        menos20 = menos20 + 1
media = soma / 4
print('A média da idade do grupo é {}.'.format(media))
print('O homem mais velho é o {}.'.format(omaisvelho))
print('{} mulheres tem menos de 20 anos.'.format(menos20))
