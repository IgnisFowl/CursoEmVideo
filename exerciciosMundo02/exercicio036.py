casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar o empréstimo? '))
prestacao = casa/(anos*12)
print('Prestação: {:.2f}'.format(prestacao))
print('30% do salário: {}'.format(salario*30/100))
if prestacao <= salario*30/100:
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi negado.')