'''frase = str(input('Digite uma frase: ')).strip().lower()
fraser = reversed_string = frase[::-1]
print(fraser)
if frase == fraser:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')'''

'''frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
fraser = junto[::-1]
print('Você digitou a frase {}'.format(palavras))
print(junto)
print(fraser)
if junto == fraser:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')'''

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('Você digitou a frase {}'.format(palavras))
print(junto, inverso)
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')