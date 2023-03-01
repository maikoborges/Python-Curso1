notas = []
media = []
todos = []

while True:
    nomes = input('Digite o nome do aluno: ')
    notas.append(float(input('Qual a primeira nota: ')))
    notas.append(float(input('Qual a segunda nota: ')))

    media.append(nomes)
    media.append(notas[:])
    media.append((notas[0] + notas[1]) / 2)
    notas.clear()

    todos.append(media[:])
    media.clear()

    cond = input('Deseja continuar [S/n]: ').lower().strip()[0]
    while cond != 'n' and cond != 's':
        print('CONDIÇÃO ERRADA, TENTE NOVAMENTE!')
        cond = input('Deseja continuar [S/N]: ').lower().strip()[0]
    print('=' * 40)
    if cond == 'n':
        break

print(f'{"Boletim Escolar":^40}')
print('=' * 40)

print(f'{"N°":<4} {"Nomes":<15} {"Média"}')
print('-' * 30)
for x in range(len(todos)):
    print(f'{x:<5}', end='')
    print(f'{todos[x][0]:<16}', end='')
    print(todos[x][2])

print('-' * 30)
x = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
while x != 999:
    print(f'Notas de {todos[x][0]} são {todos[x][1]}')
    x = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

print(f'finalizando...')
print(f'{"<<<VOLTE SEMPRE>>>"}')
