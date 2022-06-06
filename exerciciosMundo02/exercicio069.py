c = 1
maior = mulh = homens = 0
while True:
    idade = int(input(f'Digite a idade da {c}a pessoa: '))
    if idade > 18:
        maior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Digite o sexo da {c}a pessoa: [F/M] ')).strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 18:
        mulh += 1
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
    c += 1
print(f'''Quantas pessoas tem mais de 18 anos? {maior} pessoas.
Quantos homens foram cadastrados? {homens} homens.
Quantas mulheres tem menos de 20 anos? {mulh} mulheres.''')
