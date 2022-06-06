t = ('Alagoas', 'Amapa', 'Ceara', 'Bahia', 'Distrito Federal')

for c in t:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
