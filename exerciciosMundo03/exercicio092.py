from datetime import datetime
'''pessoas = {}
while True:
    pessoas["nome"] = str(input('Nome: '))
    x = int(input('Ano de Nascimento: '))
    z = 2022 - x
    pessoas["idade"] = z
    pessoas["ctps"] = int(input('CTPS (0 para pular): '))
    if pessoas["ctps"] == 0:
        pessoas["aposentadoria"] = 65-pessoas["idade"]
        print(f'Você poderá se aposentar daqui a {pessoas["aposentadoria"]} anos.')
        break
    else:
        pessoas["anocontr"] = int(input('Ano de contratação: '))
        pessoas["salario"] = float(input('Salário: R$'))
        pessoas["aposentadoria"] = (pessoas["anocontr"]+35)-x
        print(f'Você poderá se aposentar com {pessoas["aposentadoria"]} anos.')
        break'''

dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('CTPS (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade']+ ((dados['contratacao'] + 35) - datetime.now().year)
print('~*'*10)
for k, v in dados.items():
    print(f' {k} : {v}')