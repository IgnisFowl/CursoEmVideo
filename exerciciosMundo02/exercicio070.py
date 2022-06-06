total = maismil = maisbaratopreco = 0
c = 1
maisbaratonome = ''
print('~'*20, '\nGUANABARA CALCULATOR\n','~'*20)
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o valor do produto: R$'))
    total += preco
    if c == 1:
        maisbaratopreco = preco
    if preco > 1000:
        maismil += 1
    if preco < maisbaratopreco:
        maisbaratonome = nome
        maisbaratopreco = preco
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
    c += 1
print(f'O total gasto com a compra foi: R${total}.'
      f'\nQuantos produtos custam mais de R$1000? {maismil} produto(s).'
      f'\nQual o nome do produto mais barato? {maisbaratonome}, que custa R${maisbaratopreco}.')
print('{:-^50}'.format('FIM DO PROGRAMA'))