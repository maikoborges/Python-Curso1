def fatorial(num, show=False):
    """
    -> Calcular o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (Opicional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    print('=' * 40)
    fat = 1
    for x in range(num, 0, -1):
        fat *= x
    if show:
        while True:
            print(f'{ num}', end=' ')
            num -= 1
            if num == 0:
                break
            print('x', end=' ')
        return f'= {fat}'
    else:
        return fat


print(fatorial(5))
