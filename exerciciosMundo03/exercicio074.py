from random import randint
x = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100) )
print(x)
c = sorted(x)
print(f'O maior número foi {c[4]}, e o menor foi {c[0]}.')
print(f'O maior número foi {max(x)} e o menor foi {min(x)}.')