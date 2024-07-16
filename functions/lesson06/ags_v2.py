nomes = ['nome: ','Mariano']
idades = ['idade: ',28]
custos = ['custos',203]

def exibir(*args):
    for i in range(1,len(args[0])):
        for j in range(len(args[i])):
            print(args[j][0], args[j][i])


exibir(nomes, idades, custos)