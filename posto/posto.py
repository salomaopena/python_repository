

def cadastro_posto(nome_posto,salario_fixo,combustiveis,frentistas):
    posto_dados = {
        'nome':nome_posto,
        'combustiveis':combustiveis,
        'frentistas':frentistas,
        'faturamento':0,
        'bloqueado':False,
        'salario_fixo':salario_fixo
    }
    return posto_dados


def consumo(valor,combustivel, posto_dados):
    combustivel = posto_dados['combustiveis'][combustivel]
    consumido = valor / combustivel['preco']
    combustivel['volume'] -= consumido
    if combustivel['volume'] < 0:
        return False
    else:
        return float(f"{combustivel['volume']:.2f}")


def abastecer(frentista,combustivel,valor,posto_dados):
    posto_dados['frentistas'][frentista]['num_vendas'] += 1
    posto_dados['combustiveis'][combustivel]['volume'] = consumo(valor,combustivel,posto_dados)
    if not posto_dados['combustiveis'][combustivel]['volume'] == False:
        posto_dados['faturamento'] += valor
    else:
        return 'Não foi possivel abastecer...'