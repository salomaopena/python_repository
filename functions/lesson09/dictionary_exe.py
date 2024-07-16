#Dictionaries
# Create a dictionary

pessoa = {
    'nome':'Jose',
    'idade':35,
    'cidade':'Lubango',
    }

#print(pessoa)
print(f'O {pessoa['nome']} tem {pessoa['idade']} anos de idade e mora na cidade de {pessoa['cidade']}')

#Update values using an input
print('\n'*10)
nova_idade = int(input('Qual é a sua idade actual? '))
nova_cidade = input('Qual é a cidade onde mora? ')

pessoa['idade'] = nova_idade
pessoa['cidade'] = nova_cidade

print('\n'*5)

#print(pessoa)

print(f'O {pessoa['nome']} tem {pessoa['idade']} anos de idade e mora na cidade de {pessoa['cidade']}')



