def metade(v=0, cond=False):
    met = v / 2
    if cond:
        return moeda(met)
    else:
        return met


def dobro(v=0, cond=False):
    dob = v * 2
    if cond:
        return moeda(dob)
    else:
        return dob


def aumentor(v=0, t=0, cond=False):
    aum = ((v * t) / 100) + v
    if cond:
        return moeda(aum)
    else:
        return aum


def diminuir(v=0, t=0, cond=False):
    dim = v - ((v * t) / 100)
    if cond:
        return moeda(dim)
    return dim


def moeda(v=0, mod='R$'):
    cifra = f'{mod} {v:.2f}'.replace('.', ',')
    return cifra


def resume(v=0, aum=0, dim=0):
    print(f'=' * 40)
    print(f'{"RESUMO DE VALOR"}'.center(40))
    print(f'=' * 40)
    print(f'Preço analisado:   \t{moeda(v)}')
    print(f'Dobro do preço:    \t{dobro(v, True)}')
    print(f'Metade do preço:   \t{metade(v, True)}')
    print(f'{aum}% de aumento:  \t{aumentor(v, aum, True)}')
    print(f'{dim}% de redução:  \t{diminuir(v, dim, True)}')
