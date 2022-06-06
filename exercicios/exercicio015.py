d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
p = (d*60) + (km*0.15)
print('O total a pagar é: {}'.format(p))
