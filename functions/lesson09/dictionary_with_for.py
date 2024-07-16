# Dictionary using for loop

pessoa = {
    'nome':'Armando',
    'idade':35,
    'profissao':'Developer'
          }

for key in pessoa:
    print(f'Chave: {key}, Valor: {pessoa[key]}')


for key2 in pessoa.values():
    print(f'{key2}')


for key, value in pessoa.items():
    print(f'Chave: {key}, Valor: {value}')