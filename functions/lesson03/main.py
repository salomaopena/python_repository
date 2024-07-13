# Argumentos nomeados: São agumentos configurados com um valor padrão de criação

#def msg(texto, estado=1):
 #   if estado == 1:
 #      texto2 = 'atrasada'
 #   else:
 #       texto2 = 'adiantada'
 #   print(f'A mensagem enviada foi {texto} e ela chegou {texto2}')

#msg('Autor',2)

def multa(valor, tipo = 1):
    if tipo == 1:
        valor *= 1.1
    elif tipo == 2:
        valor *= 2.1
    else:
        valor *= 3.0
    print(valor)

multa(10,2)
multa(10,5)