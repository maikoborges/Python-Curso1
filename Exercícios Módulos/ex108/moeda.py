def metade(v):
    met = v / 2
    return met


def dobro(v=0):
    dob = v * 2
    return dob


def aumentor(v=0, t=0):
    aum = ((v * t) / 100) + v
    return aum


def diminuir(v=0, t=0):
    dim = v - ((v * t) / 100)
    return dim


def moeda(v=0, mod='R$'):
    cifra = f'R$ {mod} {v:.2f}'.replace('.', ',')
    return cifra
