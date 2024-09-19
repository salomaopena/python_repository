import posto as pt
from dados import *

combustiveis = ler_combustives('combustivel.csv')
frentistas = ler_frentistas('frentistas.csv')


print('***BEM-VINDO AO SOFTWARE DE GESTÃO DO SEU POSTO***')

nome_posto = input('Informe o nome do seu posto: ')
salario_fixo = float(input('Informe o salário fixo  de cada frentista: '))

posto_dados = pt.cadastro_posto(nome_posto,salario_fixo,combustiveis,frentistas)

pt.abastecer('Salomão','etanol',400,posto_dados)

#print(posto_dados)

def operacao(op,posto_dados):
    if op == 1:
        frentista = input('Informe o nome do frentista: ')
        combustivel = input('Informe o combustivel que deseja abastecer: ')
        valor = float(input('Informe o valor que será abastecido: '))
        pt.abastecer(frentista,combustivel,valor,posto_dados)
        return 'Abastecimento Realizado com Sucesso!'
    elif op == 2:
        if posto_dados['bloqueado']:
           return 'O posto já está bloqueado.'
        else:
            posto_dados['bloqueado'] = True
            return 'O posto acaba de ser bloqueado.'
    elif op == 3:
        if not posto_dados['bloqueado']:
           return 'O posto já está desbloqueado.'
        else:
            posto_dados['bloqueado'] = False
            return 'O posto acaba de ser desbloqueado.'
    elif op == 4:
        pass
    elif op == 5:
        if op ==



while True:
    ler_txt('dialogo.txt')
    try:
        opcao = int(input('Digite o número da operação que deseja Realizar: '))
    except:
        continue
    if opcao == 5:
        break
    resposta = operacao(opcao,posto_dados)
    print(resposta,posto_dados)