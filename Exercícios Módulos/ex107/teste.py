import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O doblo de {p} é {moeda.dobro(p)}')
print(f'Aumento de 10% de {p} temos {moeda.aumentor(p, 10)}')
print(f'Reduzindo 13% de {p} temos {moeda.diminuir(p, 13)}')
