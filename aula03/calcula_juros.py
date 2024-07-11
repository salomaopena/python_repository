print('Calculo Juros')

capital_inicial = float(input('Informe o capital inicial: '))
taxa = float(input('Informe a taxa: '))
meses = int(input('Informe a quantidade de meses que deseja: '))

# Calculo da taxa em percentagem
taxa = taxa/100

valor_obtido = capital_inicial* (1+taxa) ** meses

print(f'Taxa de juros de {taxa*100}% de um capital de {capital_inicial} kwanzas apos {meses} é {valor_obtido:.2f}')