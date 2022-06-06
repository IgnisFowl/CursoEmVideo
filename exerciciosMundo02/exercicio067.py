n = 1
c = 0
while n > 0:
    n = int(input('Digite o número que deseja ver a tabuada: '))
    if n < 0 or n == 0:
        break
    for c in range(1,11):
        print(f'{c:2} x {n:2} = {c*n:2}')
print('fim')