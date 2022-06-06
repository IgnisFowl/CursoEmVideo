def escreva(txt):
    b = len(txt) +4
    print('~'*b)
    print(f'  {txt}')
    print('~'*b)


txt = str(input('Digite o texto: '))
escreva(txt)