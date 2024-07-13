
lista = []

while True:
    a = int(input('Informe um elemento: '))
    if a == 10:
        break
    lista.append(a)

print(lista)


## Substituir valor na posicao
lista2 = [1,2,3,4,5,6,7,8,9]
val = int(input('Entre com um número: '))
posix = int(input('Entre com a posição: '))

lista2[posix] = val

print(lista2)