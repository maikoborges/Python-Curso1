num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))
    cod = input('Deseja continuar [S/N]? ').lower().strip()[0]
    while cod != 's' and cod != 'n':
        print('Condição errada, tente novamente!')
        cod = input('Deseja continuar [S/N]? ').lower().strip()[0]
    if cod == 'n':
        break

for x in num:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print('=' * 30)
print(f'Esta é a lista geral {num}')
pares.sort()
print(f'Esta é a lista com os números pares {pares}')
impares.sort()
print(f'Esta é a lista com os números impares {impares}')
