pessoas = []
todos = []

menor = maior = 0
while True:
    pessoas.append(input('Qual o seu nome: '))
    pessoas.append(float(input('Qual o seu peso: KG ')))
    if len(todos) == 0:
        maior = pessoas[1]
        menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    todos.append(pessoas[:])
    pessoas.clear()

    cond = input('Deseja continuar [S/N]? ').lower().strip()[0]
    while cond != 'n' and cond != 's':
        print('CONDIÇÃO ERRADA, TENTE NOVAMENTE!')
        cond = input('Deseja continuar [S/N]? ').lower().strip()[0]

    if cond == 'n':
        break
    print('=' * 40)

print('=' * 40)
print(f'Foram cadastrados {len(todos)} pessoas')
print(f'O maior peso foi de {maior} KG. Peso de ', end='')
for x in todos:
    if x[1] == maior:
        print(f'[{x[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor} KG. Peso de ', end='')
for x in todos:
    if x[1] == menor:
        print(f'[{x[0]}] ', end='')
print()
