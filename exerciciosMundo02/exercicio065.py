resposta = 'S'
soma = c = maior = menor = 0
while resposta == 'S':
    x = int(input('Digite um número: '))
    soma += x
    c += 1
    if c == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    resposta = str(input('Deseja continuar [S]/[N]? ')).strip().upper()
print('''A soma dos {} números digitados foi: {}, e a média foi: {}.
O maior número digitado foi: {}.
O menor número digitado foi: {}'''.format(c, soma, soma / c, maior, menor))
