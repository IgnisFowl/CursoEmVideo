p = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25)
print('-'*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*30)
for c in range (0,7,2):
    print('{:.<20}R$ {:>.2f}'.format(p[c],p[c+1]))