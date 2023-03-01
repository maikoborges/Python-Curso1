produtos = ('carne', 40, 'ovos', 15, 'leite', 5, 'biscoito', 2, 'sal', 1)

print('='*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('='*50)

for x in range(0, len(produtos), 2):
    print(f'{produtos[x]:.<42}', end='R$ ')
    print(f'{produtos[x+1]:5.2f}')
print('='*50)
