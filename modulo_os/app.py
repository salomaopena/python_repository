# importando a biblioteca OS
import os

# Caminho relativo
global_path = 'C:\\projetos\\python_repository\\modulo_os\\'
# mostra se o ficheiro existe no diretório do caminho especificado
show_path = os.path.exists(global_path+'app.py')
print(show_path)

relativo = 'main.py'

caminho_completo = global_path + relativo

print(os.path.join(global_path, relativo))

print(os.path.getsize(caminho_completo))


