print('{:-^50}'.format('DIGITE QUATRO NÚMEROS'))
num = (int(input('Primeiro: ')), int(input('Segundo: ')), int(input('Terceiro: ')), int(input('Quarto: ')))
print(num)

print(f'O número nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor três apareceu na posição {num.index(3) + 1}')
else:
    print('O número três não foi digitado nenhuma vez')

print('Estes foram os valores pares digitados:', end=' ')
tot = 4
for x in num:
    if x % 2 == 0:
        print(x, end=' ')
        tot += 1

    tot -= 1
    if tot == 0:
        print('NENHUM NÚMERO PAR FOI DIGITADOS')
