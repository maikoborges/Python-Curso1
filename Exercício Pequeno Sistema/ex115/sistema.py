from ex115.arquivo import *
from ex115 import dados, cores

ar = 'arquivocursoemvideo.txt'

if not arquivoExiste(ar):
    criarArquivo(ar)

while True:
    dados.menu()
    try:
        opcao = int(input(f"{cores.verde()}Sua opção: {cores.limpa()}"))
    except:
        print(f'{cores.vermelho()}ERRO! Opção inválida tente novamente.{cores.limpa()}')
    else:
        if opcao == 1:
            lerArquivo(ar)
        elif opcao == 2:
            dados.menuCadastro()
            while True:
                nome = input('Nome: ')
                if not nome.isalpha():
                    print(f'{cores.vermelho()}ERRO! Digite um nome válido.{cores.limpa()}')
                else:
                    break
            while True:
                try:
                    idade = int(input('Idade: '))
                except:
                    print(f'{cores.vermelho()}ERRO! Digite uma idade válida.{cores.limpa()}')
                else:
                    arquivoCadastrar(ar, nome, idade)
                    break
        elif opcao == 3:
            print('=' * 50)
            print(f'{"Saindo do sistema... Até logo!"}'.center(50))
            print('=' * 50)
            break
        else:
            print(f'{cores.vermelho()}ERRO! Digite uma opção válida!{cores.limpa()}')
