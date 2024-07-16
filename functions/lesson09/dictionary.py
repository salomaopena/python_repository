#Hi guys,
# In this lesson I will show you how to use dictionary in python


# Creating a dictionary

pessoa = {"nome": "John", "idade": 30, "profissao": "Developer"}

# Accessing dictionary values

print(pessoa["nome"])  # Output: John
print(pessoa["idade"])  # Output: 30
print(pessoa["profissao"])  # Output: Developer


# Updating dictionary values    

pessoa["nome"] = "Jane"
print(pessoa["nome"])  # Output: Jane


# Deleting dictionary values

del pessoa["idade"]
print(pessoa)  # Output: {'nome': 'Jane', 'profissao': 'Developer'}


# Checking if a key exists in dictionary

if "idade" in pessoa:
    print("A chave 'idade' existe no dicionário")
else:
    print("A key 'idade' não existe no dicionário")
