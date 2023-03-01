gols = []
total = 0
dados = {'nome': input('Qual o nome do jogador: ')}
quant = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for x in range(1, quant+1):
    gol = int(input(f'Quantos gols na partida {x}?: '))
    gols.append(gol)
    total += gol

dados['gols'] = gols
dados['total'] = total

print('=' * 50)
print(dados)
print('=' * 50)

for c, v in dados.items():
    print(f'O campo {c} tem o valor {v}.')

print('=' * 50)
print(f'O jogador {dados["nome"]} jogou {quant} partidas.')
for x in range(1, quant+1):
    print(f'    => Na partida {x}, fez {gols[x-1]} gols.')

print(f'Foi um total de {total} gols.')
