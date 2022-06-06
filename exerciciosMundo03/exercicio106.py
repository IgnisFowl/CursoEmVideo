c= ('\033[m',
    '\033[7;30;41m',
    '\033[0;30;45m',
    '\033[0;30;43m'
    );

def ajuda(com):
    titulo(f'Acessando o manual do comendo \'{com}\'', 2)
    print(c[3], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'* tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 2)