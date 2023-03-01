from time import sleep
print('{:-^60}'.format('ANALISANDO A TABELA DO BRASILEIRÃO'))
times = ('SPORT', 'SÃO PAULO', 'CORINTHIANS', 'PALMEIRAS', 'CRUZEIRO', 'ATLETICO MINEIRO', 'ATLÉTICO PARANAESE',
         'SANTOS', 'VASCO', 'FLUMINESE', 'FLAMENGO', 'BOTAFOGO', 'BAHIA', 'INTERNACIONAL', 'GRÊMIO', 'CHAPECOENSE',
         'AMÉRICA MINEIRO', 'VITÓRIA', 'CEARÁ', 'FORTALEZA')

print('-'*50)
print('TABELA POR COLOCAÇÃO')
print(times)

print('-'*50)
print('ESTES SÃO OS CINCO PRIMEIROS COLOCADOS CLASSIFICADOS PARA A LIBERTADORES')
sleep(1)
for x in range(0, 5):
    print(f'{x+1}° = {times[x]}')

print('-'*50)
print('ESTES SÃO OS QUATRO ÚLTIMOS QUE SERAM REBAIXADOS')
sleep(1)
for x in range(16, 20):
    print(f'{x+1}° = {times[x]}')

print('-'*50)
print('ESTÁ É A TABELA EM ORDEM ALFABÉTICA')
sleep(1)
print(sorted(times))

print('-'*50)
print('ESTA É A POSIÇÃO DO TIME DA CHAPECOENSE')
sleep(1)
pos = times.index('CHAPECOENSE')
print(f'Se enconta na posição {pos+1}°')
