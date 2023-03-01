lista = input('Digite sua expressão: ')
lista.split()

cont = cont1 = 0
for x in lista:
    if '(' in x:
        cont += 1
    if ')' in x:
        cont1 += 1

if cont != cont1 or lista[len(lista)-1] == '(' or lista[0] == ')':
    print('Esta expressão esta errada!')
else:
    print('Esta expressão esta correta!')
