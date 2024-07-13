# function SUM
import  os
def sum(a, b):
    return (a+b)

while True:
    a = int(input('Informe o valor 1: '))
    b = int(input('Informe o valor 2: '))
    c = sum(a,b)
    print(f'A soma entre {a} e {b} é: {c}')
    clear = int(input('Digite 1 para limpar a tela e 0 para sair: '))
    if clear == 1:
        os.system('clear') or None
        continue
    elif clear == 0:
        break

