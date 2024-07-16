
# Importing necessary libraries
import os
# HI GUYS,
# In this lesson I will show you how to building a stock projec using python.


# Creating a dictionary to store stocks

stocks = {}

# Create funtion for Adding stocks


def add_stock(code, name, quantity, price):
    stocks[code] = {
        'name': name,
        'quantity': quantity,
        'price': price
    }


# Create function for updating stocks


def update_stock(code, quantity, price):
    if code in stocks:
        stocks[code]['quantity'] = quantity
        stocks[code]['price'] = price
    else:
        print(f'O poduto com o codigo {code} nao existe')


# Create function for select stocks by code


def select_stock(code):
    if code in stocks:
        for key, value in stocks[code].items():
            print(f'{key}: {value}')
    else:
        print(f'O poduto com o codigo {code} nao existe')



# Create function for selling stocks


def sell_stock(code, quantity):
    if code in stocks:
        if stocks[code]['quantity'] >= quantity:
            stocks[code]['quantity'] -= quantity
        else:
            print(f'Nao ha quantidade suficiente do produto com o codigo {code}')
    else:
        print(f'O poduto com o codigo {code} nao existe')

# Create function for purchasing stocks

def purchase_stock(code, quantity):
    if code in stocks:
        if stocks[code]['quantity'] >= quantity:
            stocks[code]['quantity'] -= quantity
        else:
            print(f'Nao ha quantidade suficiente do produto com o codigo {code}')
    else:
        print(f'O poduto com o codigo {code} nao existe')


# Create function for removing stocks


def remove_stock(code):
    if code in stocks:
        del stocks[code]
    else:
        print(f'O poduto com o codigo {code} nao existe')


# Create function for displaying stocks


def display_stocks():
    for code, stock in stocks.items():
        print(f'Codigo: {code}, Nome: {stock["name"]}, Quantidade: {stock["quantity"]}, Preco: {stock["price"]}')


# Test the functions

#add_stock('AAPL', 'Apple Inc.', 100, 150.0)
#add_stock('GOOGL', 'Google Inc.', 50, 1200.0)
#display_stocks()
#update_stock('AAPL', 150, 140.0)
#display_stocks()


#sell_stock('AAPL', 50)
#purchase_stock('AAPL', 30)
#remove_stock('GOOGL')
#display_stocks()


while True:
    print('\n1 - Adicionar produto')
    print('2 - Atualizar produto')
    print('3 - Selecionar produto')
    print('4 - Vender produto')
    print('5 - Comprar produto')
    print('6 - Remover produto')
    print('7 - Mostrar produto')
    print('0 - Sair\n')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        code = int(input('Informe o codigo do produto: '))
        name = input('Informe o nome do produto: ')
        quantity = int(input('Informe a quantidade do produto: '))
        price = float(input('Informe o preco do produto: '))
        add_stock(code, name, quantity, price)
    elif opcao == 2:
        code = input('Informe o codigo do produto: ')
        quantity = int(input('Informe a nova quantidade do produto: '))
        price = float(input('Informe o novo preco do produto: '))
        update_stock(code, quantity, price)
        display_stocks()
        input('Pressione Enter para continuar...')
        os.system('cls')  # Clear the console
        continue
    elif opcao == 3:
        code = input('Informe o codigo do produto: ')
        select_stock(code)
        input('Pressione Enter para continuar...')
        os.system('cls')  # Clear the console
        continue
    elif opcao == 4:
        code = input('Informe o codigo do produto: ')
        quantity = int(input('Informe a quantidade do produto: '))
        sell_stock(code, quantity)
        display_stocks()
        input('Pressione Enter para continuar...')
        os.system('cls')  # Clear the console
        continue
    elif opcao == 5:
        code = input('Informe o codigo do produto: ')
        quantity = int(input('Informe a quantidade do produto: '))
        purchase_stock(code, quantity)
        display_stocks()
        input('Pressione Enter para continuar...')
        os.system('cls')  # Clear the console
        continue
    elif opcao == 6:
        code = input('Informe o codigo do produto: ')
        remove_stock(code)
        display_stocks()
        input('Pressione Enter para continuar...')
        os.system('cls')  # Clear the console
        continue
    elif opcao == 7:
        display_stocks()
        input('Pressione Enter para continuar...')
        os.system('cls')  # Clear the console
        continue
    elif opcao == 0:
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida!')
        print('\n'*10)
        os.system('cls')  # Clear the console
        continue
    os.system('cls')  # Clear the console
    display_stocks()

    input('Pressione Enter para continuar...')
    os.system('cls')  # Clear the console
    continue

# That's all folks! Enjoy your stock project!
