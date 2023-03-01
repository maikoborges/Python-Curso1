from random import randint
from time import sleep
from operator import itemgetter

lista = []
dic = {'Jogador1': randint(1, 6),
       'Jodador2': randint(1, 6),
       'Jogador3': randint(1, 6),
       'Jogador4': randint(1, 6)}
print('VALORES SORTEADOS')
for x, j in dic.items():
    print(f'{x} tirou {j} no dado')
    sleep(1)

lista = sorted(dic.items(), key=itemgetter(1), reverse=True)
print('O RANKING FIXOU ASSM')
for x, j in enumerate(lista):
    print(f'{x+1}° lugar: {j[0]} com {j[1]}')
    sleep(1)
