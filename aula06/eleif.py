# O USO DO ELIF

print('Trabalhando com ELIF')

# Esta condicao é utilizada para condicionais em cadeia

numero = int(input('Informe um numero múltimplo de 5: '))

if numero % 5 == 0:
    print(f'O número {numero} é múltimplo de 5')
elif numero % 3 == 0:
    print(f'O número {numero} é múltiplo de 3')
else:
    print('Caso inválido')