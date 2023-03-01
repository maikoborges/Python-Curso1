numero = []

for x in range(0, 5):
    num = int(input(f'Digite o {x}° número: '))
    if x == 0 or num > numero[len(numero) - 1]:
        numero.append(num)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(numero):
            if num <= numero[pos]:
                numero.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1

print('=' * 40)
print(f'Esta é a lista ordenada {numero}')
