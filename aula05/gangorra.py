print('Gangorra')

peso1 = int(input('Entre com o peso 1: '))
comprimento1 = int(input('Entre com o comprimento 1: '))

peso2 = int(input('Entre com o peso 2: '))
comprimento2 = int(input('Entre com o comprimento 2: '))

lado_esquerdo = peso1 * comprimento1
lado_direito = peso2 * comprimento2

if lado_direito == lado_direito:
    print(0)
elif lado_esquerdo > lado_direito:
    print(-1)
elif lado_esquerdo < lado_direito:
    print(1)