from datetime import date
x = int(input('Em que ano o atleta nasceu? '))
ano = date.today().year
y = ano - x
print('Seu atleta tem {} anos.'.format(y))
if y <= 9:
    print('A categoria é MIRIM')
elif y <= 14:
    print('A categoria é INFANTIL')
elif y <= 19:
    print('A categoria é JUNIOR')
elif y <= 20:
    print('A categoria é SENIOR')
else:
    print('A categoria é MASTER')
