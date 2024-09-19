import os 

# monstrando o nome do sistema operativo
os_name = os.name
# mostra o caminho absoluto de um diretório
path = os.getcwd()
# imprimindo os resultados
print(path)
print(os_name)
# imprime os arquivos contidos no diretório
print(os.listdir(path))
# criar um diretório no caminho especificado
print(os.mkdir(path+'\\pastateste'))