# LEN, POP, INSERT,DEL, REMOVE

#LEN Show the lenght of list

#lista = [1,2,3,4,5,6,7,8,9]
#print(len(lista))

#POP remove an element in list
#lista = [1,2,3,4,5,6,7,8,9]
#lista.pop()
#print(lista)

#lista = [1,2,3,4,5,6,7,8,9]
#lista.pop(2)
#print(lista)

#lista = [1,2,3,4,5,6,7,8,9]
#lista.insert(9,10)
#print(lista)

#lista = [1,2,3,4,5,6,7,8,9]
#del lista [2]
#print(lista)


#lista = [1,2,3,4,5,6,7,8,9]
#lista.remove(2)
#print(lista)

#lista = [1,2,3,4,5,6,7,8,9]
#print(lista[-1])


lista = [1,2,3,4,5,6,7,8,9]
lista2 = []
for i in range(3):
    lista2.append(lista[i])
print(lista2)

lista3 = lista[0:3:1] # start, top, step
print(lista3)

lista4 = lista[::-1]
print(lista4)