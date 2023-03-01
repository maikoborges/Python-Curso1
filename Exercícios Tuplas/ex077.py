palavras = ('vida', 'casa', 'terreno', 'carro', 'lugar', 'apartamento', 'viajem',
            'comida', 'festa', 'estudo', 'programador', 'dinheiro', 'paz', 'saude', 'lazer')
cont = 0
for x in palavras:
    print(f'\nNa palavra {x.upper()} temos', end=' ')
    for j in x:
        if j in 'aeiou':
            print(j, end=' ')
