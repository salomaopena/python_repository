# Working with args in python
#Hi guys, in this lesson I will show you how to use args in python.

def soma(a,b):
    # *args is a special syntax in Python that allows us to pass a variable number of arguments to a function.
    # The arguments are treated as a tuple.
    # The function will print all the arguments.
    c = a+b
    print(f"Soma de {a} e {b} é {c}")
    #print("Soma dos argumentos:", *args)

soma(2,5)

def soma_inteligente(*args):
    result = 0
    for element in args:
        result += element
    print(result) 


soma_inteligente(1,4,5)
soma_inteligente(1,4,5,6,7,8,9,10)

#kwargs is a dictionary that allows us to pass a variable number of keyword arguments to a function.


