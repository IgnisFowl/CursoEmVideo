from datetime import date
x = int(input('Em que ano você nasceu? '))
ano = date.today().year
y = ano - x
if y == 18:
    print('É hora de se alistar!')
elif y < 18:
    print('Falta(m) {} ano(s) para você se alistar.'.format(18 - y))
elif y > 18:
    print('Você deveria ter se alistado há {} ano(s) atrás.'.format(y - 18))