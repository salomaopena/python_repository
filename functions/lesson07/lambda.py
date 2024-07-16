# Hello guys,
# In this lesson I will  show you how to use lambda
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.


# Defining a lambda function


soma = lambda x, y: x + y

# Calling the lambda function

print(soma(5, 10))

# Now let's create a list of lambda functions

lista_lambdas = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y
]

# Using the lambda functions in a loop

for func in lista_lambdas:
    print(func(5, 10))


# You can also use lambda functions as arguments to other functions

def apply_func(func, x, y):
    return func(x, y)

print(apply_func(lambda x, y: x + y, 5, 10))