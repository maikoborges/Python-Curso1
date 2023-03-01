from ex109 import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O doblo de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumento de 10% de {moeda.moeda(p)} temos {moeda.aumentor(p, 10, True)}')
print(f'Reduzindo 13% de {moeda.moeda(p)} temos {moeda.diminuir(p, 13, False)}')
