dados = {}
listaNome = []
lista = []
quant = total = 0
while True:
    nome = input('Qual o nome: ')
    dados['nome'] = nome
    sexo = input('Qual o sexo: [M/F] ').lower().strip()[0]
    while sexo != 'f' and sexo != 'm':
        print('Tentativa Errada, tente novamente!')
        sexo = input('Qual o sexo: [M/F] ')
    dados['sexo'] = sexo
    idade = int(input('Qual a idade: '))
    dados['idade'] = idade
    quant += 1
    total += idade
    if sexo == 'f':
        listaNome.append(nome)
    lista.append(dados.copy())

    cond = input('Deseja continuar [S/N]: ').lower().strip()[0]
    while cond != 's' and cond != 'n':
        print('Condição errada, tente novamente!')
        cond = input('Deseja continuar [S/N]: ').lower().strip()[0]
    if cond == 'n':
        break

media = total/quant
print('=' * 40)
print(f'- O grupo tem {quant} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
if len(listaNome) > 0:
    print(f'- As mulheres cadastradas foram: ', end='')
    for x in listaNome:
        print(x, end=' ')
    print()
else:
    print('- Nenhuma mulher cadastrada')

print('- Lista das pessoas que estão acima da média:')
for x in lista:
    if x['idade'] > media:
        print(f'    nome = {x["nome"]}; sexo = {x["sexo"]}; idade = {x["idade"]};')

print('<< ENCERRADO >>')
