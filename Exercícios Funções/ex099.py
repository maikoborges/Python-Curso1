from time import sleep


def maior(*num):
    cont = mai = 0
    while cont < len(num):
        if cont == 0:
            mai = num[cont]
        else:
            if mai < num[cont]:
                mai = num[cont]
        cont += 1
    print('=' * 50)
    print(f'Analisando os valores passados...')
    for x in num:
        sleep(0.3)
        print(x, end=' ')
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(2, 3, 7, 1, 0, 10)
maior(0, 4, 7, 8)
maior()
maior(5)
maior(0)
