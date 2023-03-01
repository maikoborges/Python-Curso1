from random import randint

num = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('Estes foram os valores sorteados: ', end='')

for x in num:
    print(x, end=' ')

print(f'\nEste é o maior número da tupla {max(num)}')
print(f'Este é o menor número da tupla {min(num)}')
