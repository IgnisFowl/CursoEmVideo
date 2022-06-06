lista = []
temp = []
media = 0
while True:
    temp.append(str(input('Nome do Aluno: ')))
    temp.append(int(input('Nota 1: ')))
    temp.append(int(input('Nota 2: ')))
    lista.append(temp[:])
    temp.clear()
    r = str(input('Deseja adicionar mais um aluno [s/n]? ')).strip().lower()[0]
    if r in 'n':
        break
print('~'*30)
print(f'{"BOLETIM":^30}')
print('~'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for c in range(0, len(lista)):
    media = (lista[c][1] + lista [c][2]) / 2
    print(f'{c:<4}{lista[c][0]:<10}{media:>8}')
print('~'*30)
while True:
    x = int(input('Deseja ver as notas de qual aluno? (999 interrompe) No: '))
    if x == 999:
        break
    if x <= len(lista) -1:
        print(f'Aluno {lista[x][0]}: \nNota 1: {lista[x][1]} \nNota 2: {lista[x][2]}.')

