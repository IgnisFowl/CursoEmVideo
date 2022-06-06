x = str(input('Digite a expressão: '))
a = f = 0
for i, v in enumerate(x):
   if x[i] == '(':
       a += 1
   elif x[i] == ')':
       f += 1
if a == f:
    print('A expressão é válida.')
else:
    print('A expressão não é válida.')

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é válida.')
else:
    print('A expressão não é válida.')