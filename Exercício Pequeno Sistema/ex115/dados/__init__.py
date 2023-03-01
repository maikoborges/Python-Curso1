from ex115 import cores, arquivo


def menu():
    print('=' * 50)
    print(f'{"MENU PRINCIPAL"}'.center(50))
    print('=' * 50)
    print(f"{cores.amarelo()}1 - {cores.azul()}Ver pessoas cadastradas")
    print(f"{cores.amarelo()}2 - {cores.azul()}Cadastrar nova pessoa")
    print(f"{cores.amarelo()}3 - {cores.azul()}Sair do sistema{cores.limpa()}")
    print('=' * 50)

def menuCadastro():
    print('=' * 50)
    print(f'{"NOVO CADASTRO"}'.center(50))
    print('=' * 50)