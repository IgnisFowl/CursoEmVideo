x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
if x > y:
    print('O primeiro número é maior.')
elif y > x:
    print('O segundo número é maior.')
elif y == x:
    print('Não existe valor maior, os dois são iguais.')