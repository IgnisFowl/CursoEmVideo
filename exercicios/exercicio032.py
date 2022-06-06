x = int(input('Digite o ano: '))
if x%100==0 and x%400==0:
    print('O ano {} é bissexto.'.format(x))
else:
    print('O ano {} não é bissexto.'.format(x))
