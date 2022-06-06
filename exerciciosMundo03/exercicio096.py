def area():
    print('Vamos calcular a área de um terreno!')
    x = float(input('Digite a largura do terreno: '))
    y = float(input('Digite o comprimento do terreno: '))
    z = x * y
    print(f'A área do terreno de {x}m de largura e {y}m de comprimento é igual a {z} metros quadrados.')

while True:
    area()
    r = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]
    if r == 'n':
        break