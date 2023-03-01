print('{:-^50}'.format('DIGITE O NÚMERO DE 0 A 20 E O VEJO POR EXTENSO'))
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'cartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número: '))
    while num < 0 or num > 20:
        print('NÚMERO INCORRENTO, TENTE NOVAMENTE!')
        num = int(input('Digite um número: '))

    print('ESTE É O NÚMERO DIGITADO ESCRITO POR EXTENSO')
    print(tupla[num])

    cod = input('Deseja continuar sim ou não? ').strip().lower()[0]
    if cod == 'n':
        break
