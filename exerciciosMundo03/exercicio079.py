valores = []
c = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado! Não será adicionado.')
    resposta = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]
    if resposta == 'n':
        break
    c += 1
valores.sort()
print(f'Os valores digitados em ordem crescente são: {valores}')