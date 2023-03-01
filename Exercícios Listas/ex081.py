num = []

while True:
    num.append(int(input('Digite um número: ')))
    cod = input('Deseja continuar [S/N]: ').lower().strip()[0]
    while cod != 's' and cod != 'n':
        print('Condição errada, tente novamente!')
        cod = input('Deseja continuar [S/N]: ').lower().strip()[0]
    if cod == 'n':
        break

print('=' * 30)
print(f'Esta é a lista completa {num}')
print(f'Foram digitados {len(num)} números')
num.sort(reverse=True)
print(f'Aqui está a lista ordenada de forma descresente {num}')
if 5 in num:
    print('O número 5 consta na lista, na posição ', end='')
    for p, v in enumerate(num):
        if v == 5:
            print(p, end='...')
            print()
else:
    print('O número 5 não consta na lista!')
