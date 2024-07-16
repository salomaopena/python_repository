#Dictionary using GET

pessoa = {
    'nome':'Jose',
    'idade':30,
    'profissao':'Developer',
    'endereco':{
        'rua':'Rua da Paz',
        'numero':123
    },
    'filhos':['Joao', 'Maria']
          }

print(pessoa.get('nome'))
print(pessoa.get('idade'))
print(pessoa.get('profissao'))
print(pessoa.get('endereco', {}).get('rua'))
print(pessoa.get('endereco', {}).get('numero'))
print(pessoa.get('filhos', ['Nenhum']))

#Dictionary using SET

pessoa['idade'] = 31
print(pessoa)

#Dictionary using DELETE

del pessoa['endereco']
print(pessoa)

#Dictionary using UPDATE

pessoa['filhos'].append('Jose')
print(pessoa)

#Dictionary using POP

pessoa.pop('idade')
print(pessoa)

#Dictionary using IN

if 'nome' in pessoa:
    print('Chave nome existe no dicionário')
else:
    print('Chave nome não existe no dicionário')

#Dictionary using LEN

print(len(pessoa))

#Dictionary using KEYS

print(list(pessoa.keys()))

#Dictionary using VALUES

print(list(pessoa.values()))

#Dictionary using ITEMS

print(list(pessoa.items()))

#Dictionary using CLEAR

pessoa.clear()
print(pessoa)

#Dictionary using COPY

pessoa_copia = pessoa.copy()
print(pessoa_copia)

#Dictionary using FROMKEYS

pessoa_novos_dados = dict.fromkeys(['nome', 'idade', 'profissao'], 'Desconhecido')
print(pessoa_novos_dados)

#Dictionary using GET OR

print(pessoa.get('idade', 'Valor padrão'))
print(pessoa.get('sexo', 'Valor padrão'))

#Dictionary using GET AND

print(pessoa.get('nome', {}).get('primeiro_nome', 'Valor padrão'))
print(pessoa.get('endereco', {}).get('cidade', 'Valor padrão'))

#Dictionary using SET DEFAULT

pessoa.setdefault('endereco', {}).setdefault('cidade', 'Cidade desconhecida')
print(pessoa)


print(pessoa.popitem())
print(pessoa)

#Dictionary using CLEAR AND GET

pessoa.clear()
print(pessoa.get('nome', 'Valor padrão'))
print(pessoa.get('idade', 'Valor padrão'))
print(pessoa.get('profissao', 'Valor padrão'))
print(pessoa.get('endereco', {}).get('rua', 'Valor padrão'))
print(pessoa.get('endereco', {}).get('numero', 'Valor padrão'))
print(pessoa.get('sexo', 'Valor padrão'))



