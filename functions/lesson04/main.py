import os
# Sistema de castro de clientes

nomes = []
idades = []
gastos = []

def cadastrar_dados():
    print('Cadastre os dados dos clientes em linhas separadas')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    gasto = float(input('Gasto: '))

    nomes.append(nome)
    idades.append(idade)
    gastos.append(gasto)
    print('Cliente cadastrado com sucesso!')
    print('\n'*10)



def listar_dados():
    print('Listando dados dos clientes \n')
    p = input('Insira o nome que deseja buscar: ')
    pos = 0
    for i in range(len(nomes)):
        if nomes[i] == p:
            print(f'Nome: {nomes[i]}, Idade: {idades[i]} anos, Gasto: {gastos[i]}')
            return 0
    print(f'Esse nome {p} não consta da lista')


def balanco():
    medias_idade = sum(idades)/len(idades)
    media_gastos = sum(gastos)/len(gastos)
    print('Os dados da sua base são: ')
    print(f'Média de idade: {medias_idade:.2f} anos')
    print(f'Média de gastos: {media_gastos:.2f} kwanzas')


# Programa principal
print('Bem vindo ao sistema de cadastro de clientes')
print('*'*40)

while True:
    print('1 - Cadastrar dados')
    print('2 - Listar dados')
    print('3 - Calcular balanço')  # Adicionado para exercício extra
    print('0 - Sair \n')
    opcao = int(input('Escolha uma opção: '))
 
    if opcao == 1:
        cadastrar_dados()
    elif opcao == 2:
        listar_dados()
    elif opcao == 3:
        balanco()
    elif opcao == 0:
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida!')
        print('\n'*10)
        os.system('clear') or None # Limpa a tela no terminal Unix/Linux

