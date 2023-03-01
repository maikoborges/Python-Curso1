gols = []
dados = {}
geral = []
while True:
    total = 0
    dados = {'nome': input('Qual o nome do jogador: ')}
    quant = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for x in range(1, quant+1):
        gol = int(input(f'Quantos gols na partida {x}?: '))
        gols.append(gol)
        total += gol
    
    dados['gols'] = gols.copy()
    gols.clear()
    dados['total'] = total
    geral.append(dados.copy())

    cond = input('Deseja continuar? [S/N] ').lower().strip()[0]
    while cond != 'n' and cond != 's':
        print('Condição errada! tente novamente')
        cond = input('Deseja continuar? [S/N] ').lower().strip()[0]
    if cond == 'n':
        break
    print('-' * 50)

print(geral)
print('=' * 50)
print(f'cod', ' ' * 5, 'nome', ' ' * 10, 'gols', ' ' * 10, 'total')
print('-' * 50)
for p, v in enumerate(geral):
    #print(f' {p:<8} {v["nome"]:<15} {v["gols"]:} {v["total"]}')   # problema de distância
    print(f'  {p:<9}', end='')
    for x in v.values():
        print(f'{str(x):<15}', end='')
    print()

print('-' * 50)
n = int(input('Mostrar dados de qual jogador? '))
while n != 999:
    for x in range(0, len(geral)):
        if n == x:
            print(f'--LEVANTAMENTO DO JOGADOR {geral[x]["nome"]}:')
            for j in range(0, len(geral[x]["gols"])):
                print(f'No jogo {j+1} fez {geral[x]["gols"][j]} gols.')
    if n > len(geral) - 1 or n < 0:
        print(f'Erro! Não existe jogador com o código {n}! Tente novamente')
    n = int(input('Mostrar dados de qual jogador? '))
print('<< VOLTE SEMPRE >>')
