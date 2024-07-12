# Trabalhando com estrutura de repetição:
# WHILE E FOR
print('ESTRUTURAS DE REPETIÇÃO')

digitos = int(input('Entre a quantidade de números: '))

dentro_invervalo = 0
fora_intervalo = 0

while digitos > 0:
    digitos -= 1
    numero = int(input(f'Informe a posição {digitos}: '))
    if numero >= 10 and numero <= 20:
        dentro_invervalo += 1
    else:
        fora_intervalo += 1

print(f'{dentro_invervalo} in')
print(f'{fora_intervalo} out')
