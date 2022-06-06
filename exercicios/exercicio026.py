frase = input('Digite uma frase: ').strip().lower()
print('Letras A: ', frase.count('a'))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição: {}'.format(frase.rfind('a')+1))
