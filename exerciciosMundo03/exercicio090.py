aluno = dict()

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input('Digite a média do aluno: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
        aluno['Situação'] = 'REPROVADO'
print("~*"*10)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
print("~*"*10)


