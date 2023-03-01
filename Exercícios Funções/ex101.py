def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 18:
        return f'Com {idade} anos: Não vota'
    elif idade < 60:
        return f'Com {idade} anos: Voto obrigatótio'
    else:
        return f'Com {idade} anos: Voto opcional'


ano = int(input(f'Em que ano você nasceu? '))
print(voto(ano))
