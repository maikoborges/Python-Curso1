def leiaInt(texto=''):
    n = input(texto)
    if n.isnumeric():
        n = int(n)
    else:
        while True:
            print(f'\033[:31mErro! digite um número inteiro válido\033[m')
            n = input('Digite um número: ')
            if n.isnumeric():
                break
    return n


a = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {a}')
