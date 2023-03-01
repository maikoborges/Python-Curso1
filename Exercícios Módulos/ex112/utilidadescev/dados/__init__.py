def leia_dinheiro(msg=''):
    cond = ''
    valor = 0
    while True:
        tipo = input(msg).replace(',', '.').strip()
        if tipo.isalpha() or tipo == '':
            print(f'\033[31mERRO: "{tipo}" é um preço inválido!\033[m')
        else:
            cond = 's'
            valor = float(tipo)
        if cond == 's':
            break
    return valor
