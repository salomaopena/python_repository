# O uso do ELIF: parte 2

print('Olimpiada de basquetebol de robôs')

numero =  int(input('Entre com um número: '))

if numero <=800:
    print(1)
elif numero > 800 and numero <= 1400:
    print(2)
elif numero > 1400 and numero <= 2000:
    print(3)

 # Outra forma de o fazer

if numero >= 1400:
    print(3)
elif numero > 800:
    print(2)
else:
    print(1)