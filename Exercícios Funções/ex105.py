def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dic = {}
    maior = menor = soma = 0
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n) / len(n)
    if sit:
        if dic['média'] < 5:
            dic['situação'] = 'RUIM'
        elif dic['média'] < 7:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'BOA'
    return dic


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
