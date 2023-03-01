from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = passo - passo * 2
    print('=' * 50)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim and passo > 0:
        passo = passo - passo * 2
    if inicio > fim:
        fim -= 1
    else:
        fim += 1
    for x in range(inicio, fim, passo):
        #sleep(0.3)
        print(x, end=' ')
    print('FIM!')


contador(1, 10, 1)

contador(10, 0, -2)

print('=' * 50)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fi = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fi, pas)
