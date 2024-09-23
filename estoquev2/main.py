# palavras reservada para criação de um objeto é 'class'
# classe Estoque
class Estoque:
    def __init__(self, nome, capacidade_maxima):
        self.nome = nome
        self.max = capacidade_maxima
        self.produtos = {}
        self.endereco = ''

def add_produto(self, id,nome,quantidade):
    if id in self.produtos:
        self.produtos[id]['nome'] += quantidade 
    else: 
        self.produtos[id]['nome'] = quantidade
    self.max -= quantidade