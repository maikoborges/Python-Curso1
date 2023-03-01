matriz = [[], [], []]
for x in range(0, 3):
    for j in range(0, 3):
        matriz[x].append(int(input(f'Preencha um número no espaço [{x}, {j}] da matriz: ')))

print('=' * 40)
print('Esta foi a matriz gerada')

pares = terc = maior = 0
for x in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[x][j]:^3} ]', end='')

        if matriz[x][j] % 2 == 0:
            pares += matriz[x][j]

        if j == 2:
            terc += matriz[x][2]

        if x == 1 and j == 0:
            maior = matriz[1][j]
        elif x == 1 and j > 0:
            if matriz[1][j] > maior:
                maior = matriz[1][j]
    print()

print(f'Esta é a soma dos números pares da matriz = {pares}')
print(f'Esta é a soma dos números da terceira coluna = {terc}')
print(f'Este é o maior número da segunda linha = {maior}')
