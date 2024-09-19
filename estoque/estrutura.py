
def adicionar_item(estoque, item, quantidade):
    if item in estoque:
        estoque[item] += quantidade
    else:
        estoque[item] = quantidade


def buscar_item(estoque,item):
    if item in estoque:
        return f'O estoque possui {estoque[item]} do item {item}'
    else:
        return f'O produto {item} não esta cadastrado no estoque'

def checar_ocupacao(estoque):
    for key, value in estoque:
        print(f"{key}:{value} unidade")
    return(len(estoque))