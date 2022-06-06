pessoas = {}
lista = []
mulheres = []
acima = []
tot = totid = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if pessoas['sexo'] not in "FfMm":
            print('Erro! Digite apenas F ou M.')
        else:
            break
    if pessoas['sexo'] == "F":
        mulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    totid += pessoas['idade']
    tot += 1
    while True:
        r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if r not in "SsNn":
            print('Erro! Responda apenas S ou N.')
        else:
            break
    if r == 'N':
        break
media = totid/tot
print('*~'*10)
print(lista)
print('*~'*10)
print(f'A. Total de pessoas cadastradas: {tot}')
print(f'B. Média de idade: {media:.2f}.')
print(f'C. Lista de mulheres: {mulheres}')
print(f'D. Lista com idade acima da média: ', end='')
for p in lista:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')
print()

print('-'*40)
print('cod ', end='')
for i in pessoas.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)