print('FLIPER')

p = int(input('Informe o numero da porta P: '))
r = int(input('Informe o numero da porta R: '))

if p == 0:
    print('C')

if p == 1 and r == 1:
    print('A')

if p == 1 and r == 0:
    print('B')