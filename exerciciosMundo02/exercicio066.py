n = s = c = 0
while True:
    n = int(input('Digite um número (e digite 999 pra parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores digitados foi {s}.')