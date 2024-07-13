# PROBLEMA DE ACENDER A LAMPADA


numero = int(input('Informe um número: '))


lista_comandos = []
a = 0
b = 0

for i in range(numero):
    x = int(input('Informe o estado do interroptor: '))
    lista_comandos.append(x)

for i in range(numero):

    comando = lista_comandos[i]

    if comando == 1:
        if a == 0:
            a = 1
        else:
            a = 0
    if comando == 2:
        if b == 0:
            b = 1
        else:
            b = 0
print(a)
print(b)
