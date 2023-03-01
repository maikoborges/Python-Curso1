from ex108 import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O doblo de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumento de 10% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentor(p, 10))}')
print(f'Reduzindo 13% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, 13))}')
