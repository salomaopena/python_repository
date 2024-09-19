import estrutura as es
estoque = {}

while True:
    print('Deseja Continuar? Digite "s" para Sim e "n" para não', end='')
    decisao = input()
    if decisao == 'n':
        break
    else:
        print('Pressione 1 para Adicionar Item')
        print('Pressione 2 para Buascar Item ')
        print('Pressione 3 pra Verificar ocupação do estoque \n')
    
        op = int(input('Digite... '))

        if op == 1:
            print('Digite o nome do Item e a quantidade a ser adicionada: ')
            item,qtd = input().split()
            qtd =int(qtd)
            es.adicionar_item(estoque,item,qtd)
        elif op == 2:
            print('Digite o nome do Item a buscar: ')
            item = input()
            es.buscar_item(estoque,item)
        elif op == 3:
            es.checar_ocupacao(estoque)
        else:
            print('Opção {op} inválida!')

print('Estoque finalizado...')