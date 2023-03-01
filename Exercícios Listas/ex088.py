from random import randint
from time import sleep
jogo = []
todosjogos = []

print('=' * 50)
print('\33[1:31m {:^50}\33[m'.format('BOLÃO DA MEGA SENA'))
print('=' * 50)

cont = 0
quant = int(input('Quantos jogos seram gerados? '))
for x in range(0, quant):
    for j in range(0, 6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)

    jogo.sort()
    todosjogos.append(jogo[:])
    jogo.clear()

print('{:=^50}'.format(' ESTES FORAM OS JOGOS GERADOS '))
for p, x in enumerate(todosjogos):
    sleep(1)
    print(f'Jogo {p+1}: {x}')
print('{:=^50}'.format('BOA SORTE'))
