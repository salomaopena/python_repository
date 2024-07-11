print('Calcula a velocidade media')

ponto_inicial = float(input('Informe a posição inicial (m): '))
ponto_final = float(input('Informe a posição final (m): '))
tempo = float(input('Informe o tempo em trajecto (s): '))

valocidade_media = (ponto_final-ponto_inicial)/tempo

print(f'Valocidade media: {valocidade_media:.1f} m/s')
