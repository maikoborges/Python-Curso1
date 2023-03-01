def arquivoExiste(nome):
    try:
        ar = open(nome, 'rt')
        ar.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        ar = open(nome, 'wt+')
        ar.close()
    except:
        print('Houve algum erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    print('=' * 50)
    print(f'{"PESSOAS CADASTRADAS"}'.center(50))
    print('=' * 50)
    try:
        ar = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        for l in ar:
            dados = l.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:30}', end='')
            print(f'{dados[1]:>3} Anos')
        ar.close()


def arquivoCadastrar(arq, nome, idade):
    try:
        ar = open(arq, 'at')
    except:
        print('Houve algum erro ao abrir o arquivo!')
    else:
        ar.write(f'{nome};{idade}\n')
        ar.close()
        print(f'Cadastrado de {nome} realizado com sucesso')
