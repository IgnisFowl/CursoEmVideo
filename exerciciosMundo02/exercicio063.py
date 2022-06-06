c = 1
n = int(input('Digite quantos elementos deseja ver da Sequência Fibonacci: '))
x = 0
y = 1
print('0', end=' ')
while c <= n-1:
    z = x + y
    y = x
    x = z
    c += 1
    print(x, end=' ')
print('\nFIM')