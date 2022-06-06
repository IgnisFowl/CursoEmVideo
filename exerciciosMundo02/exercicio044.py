print('{:=^40}'.format(' LOJAS GUANABARA '))
x = float(input('Digite o valor do produto: '))
y = int(input('''Digite a forma de pagamento: 
1. A Vista em Dinheiro/Cheque 
2. A vista no cartão 
3. Em até 2x no cartão
4. Em 3x ou mais vezes no cartão
Digite a opção desejada:  '''))
if y == 1:
    f1 = x - (x/100*10)
    print('O valor final terá 10% de desconto: R${}.'.format(f1))
elif y == 2:
    f2 = x - (x/100*5)
    print('O valor final terá 5% de desconto: R${}.'.format(f2))
elif y == 3:
    print('O valor final será R${}, dividido em parcelas de R${}.'.format(x, x/2))
elif y == 4:
    f3 = x + (x/100*20)
    parcelas = int(input('Em quantas parcelas?'))
    print('O valor final terá 20% de juros: R${}, dividido em {} parcelas de R${}.'.format(f3, parcelas, f3/parcelas))
else:
    print('Opção inválida.')