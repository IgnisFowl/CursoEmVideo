v = []
c=0
while True:
    n = int(input('Digite um valor: '))
    v.append(n)
    c += 1
    r = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]
    if r == 'n':
        break
print(f'{c} valores foram digitados.')
v.sort(reverse=True)
print(f'A lista em ordem descrescente: {v}')
if 5 in v:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista')
