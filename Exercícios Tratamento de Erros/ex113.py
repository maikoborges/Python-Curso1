def leiaInt(texto=''):
    c = ''
    while True:
        try:
            intei = int(input(texto))
        except (ValueError, TypeError):
            print(f'\033[31mErro! tente novamente\033[m')
        except KeyboardInterrupt:
            c = 'ok'
            print()
            print(f'\033[31mO usuário preferiu não digitar nada\033[m')
            return 0
        else:
            return intei


def leiaReal(texto=''):
    c = ''
    while True:
        try:
            real = float(input(texto))
        except (ValueError, TypeError):
            print(f'\033[31mErro! tente novamente\033[m')
        except KeyboardInterrupt:
            print()
            print(f'\033[31mO usuário preferiu não digitar nada\033[m')
            return 0
        else:
            return real


n = leiaInt('Digite um inteiro: ')
m = leiaReal('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {m}')
