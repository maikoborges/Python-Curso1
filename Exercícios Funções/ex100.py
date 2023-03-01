from random import randint
from time import sleep
lista = []


def soteia():
    print('Sorteando 5 valores da lista', end=' ')
    for x in range(0, 5):
        sleep(0.3)
        num = randint(1, 10)
        print(num, end=' ')
        lista.append(num)
    print('PRONTO!')


def soma():
    s = 0
    for x in lista:
        if x % 2 == 0:
            s += x
    print(f'Somando os valores pares de {lista}, temos {s}')


soteia()
soma()
