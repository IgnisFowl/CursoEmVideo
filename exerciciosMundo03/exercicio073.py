times = ('Corinthians','Santos','Avaí','América-MG','Red Bull Bragantino','São Paulo','Atlético-MG','Botafogo','Internacional','Coritiba','Cuiabá','Athletico','Palmeiras','Flamengo','Fluminense','Goiás','Ceará','Juventude','Atlético-GO','Fortaleza' )
print('Os 5 primeiros colocados:', times[0:5])
print('Os últimos 4 colocados:', times[-4:-1])
print('Em ordem alfabética:', sorted(times))
x = times.index('Palmeiras')
print(f'Palmeiras está na {x+1}a posição.')

