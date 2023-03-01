def ficha(n='', g=0):
    if n == '':
        dados = f'O jogador <desconhecido> fez {g} gol(s) no campeonato'
        return dados
    elif g == '':
        dados = f'O jogador {n} fez {g} gol(s) no campeonato'
        return dados
    else:
        dados = f'O jagador {n} fez {g} gol(s) no campeonato.'
        return dados


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(ficha(nome, gols))
