def valor(quantidade, preco):
    total = quantidade * preco
    print(total)


q = int(input('Informe a quantidade: '))
p = float(input('Informe o preco: '))

total=valor(q,p)

print (f'O total do valor é {total}') 
