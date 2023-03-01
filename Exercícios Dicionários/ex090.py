dic = {'nome': input('Qual o seu nome: ')}
nota1 = float(input('Qual a sua primeira nota: '))
nota2 = float(input('Qual a sua segunda nota: '))

media = (nota1 + nota2) / 2
dic['média'] = media
if media < 7:
    dic['situação'] = 'Reprovado'
else:
    dic['situação'] = 'Aprovado'

print(f'O aluno {dic["nome"]}')
print(f'Obteve uma média {dic["média"]:.1f}')
print(f'Ficando {dic["situação"]}')
