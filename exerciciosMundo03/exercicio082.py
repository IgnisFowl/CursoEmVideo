l1 = []
l2 = []
l3 = []
while True:
    x = int(input('Digite um valor: '))
    l1.append(x)
    r = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]
    if r == 'n':
        break
print(l1)
#for c, v in enumerate(l1):
for c in range(0, len(l1)):
    if l1[c]%2==0:
        l2.append(l1[c])
    else:
        l3.append(l1[c])
print(l2)
print(l3)
