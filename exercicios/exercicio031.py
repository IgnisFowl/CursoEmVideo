x = float(input('Digite a distância viajada: '))
if x >= 200:
    print('O valor a partir de 200km é de {}'.format(x*0.45))
else:
    print('O valor abaixo de 200km é de {}.'.format(x*0.50))