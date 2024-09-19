'''
Combustíveis={
    'gasolina':{
        'preco': 5.7,
        'volume':500
    },
    'etanol':{
        'preco': 4.7,
        'volume':200
    },
}
'''

import pandas as pd


# Ler txt
def ler_txt(arquivo):
    with open(arquivo,'r',encoding='utf-8') as file:
        print(file.read())


# Ler dados de combsutíves
def ler_combustives(arquivo):
    combustivel = {}
    dados_combustivel = pd.read_csv(arquivo)
    dados_combustivel = dados_combustivel.to_dict('records')
    for dados in dados_combustivel:
        combustivel[dados['nome']] = {
            'volume':dados['volume'],
            'preco':dados['preco']
        }
    return combustivel


# ler dados dos frentistas
def ler_frentistas(arquivo):
    frentistas = {}
    dados_frentistas = pd.read_csv(arquivo)
    dados_frentistas = dados_frentistas.to_dict('records')
    for dados in dados_frentistas:
        frentistas[dados['nome']]={
            'num_vendas':0,
            'bonus':0
        }
    return frentistas
    

def relatorio(nome,posto_dados):
    nome+='.txt'
    with open(nome,'a+',encoding='utf-8') as file:
        file.write(f'Relatório do Posto {posto_dados["nome"]}\n\n')

        file.write('Combustívieis: \n\n')
        for combustivel in posto_dados['combustiveis'].items():
            file.write(f"Tipo: {combustivel[0]}\n\n")
            file.write(f"Disponível: {combustivel[1]['volume']}\n")
            file.write(f"Preço Atual: {combustivel[1]['preco']}\n")

# Crie aqui seu código para o Frentista5



if __name__ == '__app__':   
    print(ler_frentistas('frentistas.csv'))
    print(ler_combustives('combustivel.csv'))   