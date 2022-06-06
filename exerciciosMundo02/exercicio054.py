maior = 0
menor = 0
from datetime import date
for c in range (0,7):
    x = int(input('Digite o ano de nascimento: '))
    ano = date.today().year
    idade = ano - x
    print(idade)
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Maiores de idade: {}.'.format(maior))
print('Menores de idade: {}.'.format(menor))