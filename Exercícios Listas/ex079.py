numero = []

while True:
    num = int(input('Digite um número: '))
    if num not in numero:
        numero.append(num)
        print('Adicionado')
    else:
        print('Já existe, não vou adicionar')

    cond = input('Deseja continuar [S/N]? ').strip().lower()[0]
    while cond != 's' and cond != 'n':
        print('Condição errada, tente novamente')
        cond = input('Deseja continuar [S/N]? ').strip().lower()[0]
    print('-='*20)
    if cond == 'n':
        break

numero.sort()
print(f'Você digitou os valores {numero}')
