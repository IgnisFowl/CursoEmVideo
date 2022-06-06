def ficha(jog='<desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gol} gols.')

x = str(input('Nome do Jogador: '))
y = str(input('Número de Gols: '))
if y.isnumeric():
    y = int(y)
else:
    g = 0
if x.strip()=='':
    ficha(gol=y)
else:
    ficha(x,y)