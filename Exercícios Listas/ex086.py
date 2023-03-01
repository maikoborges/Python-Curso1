matriz = [[]]
num = 0
for x in range(0, 3):
    for j in range(0, 3):
        matriz[0].append(int(input(f'Preencha o espaço [{x}, {j}] da matriz: ')))

print('=' * 40)
print('Esta foi a matriz gerada')

cont = 0
for x in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[0][cont]:^3} ]', end='')
        cont += 1
    print()
