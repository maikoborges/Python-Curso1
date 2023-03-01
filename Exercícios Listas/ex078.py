valores = []
pos = []
pos1 = []

maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v}° valor: ')))
    if v == 0:
        maior = valores[v]
        menor = valores[v]
    else:
        if valores[v] >= maior:
            maior = valores[v]
        if valores[v] <= menor:
            menor = valores[v]

print('=' * 50)
print(f'A lista criada contém os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(p, end='...')

print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(p, end='...')
print()
