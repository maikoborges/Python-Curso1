cores = ('\033[m',
         '\033[41m',
         '\033[42m',
         '\033[43m',
         '\033[44m')


def ajuda(c):
    stilo(f'   Acessando o manual do \'{c}\'', 3)
    print(cores[4], end='')
    help(c)


def stilo(msg, cor=0):
    print(cores[cor], end='')
    print('~' * (len(msg) + 3))
    print(msg)
    print('~' * (len(msg) + 3))


while True:
    stilo('   SISTEMA DE AJUDA PYHELP', 2)
    com = input(f'{cores[0]}Função ou Biblioteca > ').lower()
    if com == 'fim':
        break
    else:
        ajuda(com)

stilo('   FIM', 1)

