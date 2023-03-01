from datetime import date

dados = {'nome': input('Qual o seu nome: ')}
nasc = int(input('Qual o seu ano de nascimento: '))
atual = date.today()
idade = atual.year - nasc
dados['idade'] = idade
dados['ctps'] = int(input('N° da carteira de trabalho (0 se não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Qual o ano da contratação: '))
    dados['salario'] = float(input('Qual o salário: '))
    apos = (dados['contratação'] + 35) - nasc
    dados['aposentadoria'] = apos

print('=' * 40)
for d, v in dados.items():
    print(f'{d} tem o valor {v}')
