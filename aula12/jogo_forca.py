# Exibir mensagem
print('Iniciando o Jogo da Forca\n')
# preencher a palavra-chave
palavra = input('Insira  a palavra-chave do jogo: ')
# Prencher a quantidade de vidas que terá no jogo
vidas = int(input('Insira a quantidade de vida: '))

print('\n'*100)

print('O jogo já está configurado. Comece as suas tentativas')
print(f'Você tem {vidas} tentativas para errar')

aux = '*'*len(palavra)
print(f'A palavra é do seguinte formato: {aux}')

letras_usadas = []

while True:
    #pemitir a entrada de uma letra
    letra = input('Insira uma letra: ')
    #verificar se a palavra já foi digitada

    if letra in letras_usadas:
        print(f'A letra {letra} já foi utilizada.')
    else:
        letras_usadas.append(letra)

    # Verificar se a letra estiver na palvra

    if letra in palavra:
        print(f' A letra {letra} está na palavras.')
        frase = ''
        for l in palavra:
            if l in letras_usadas:
                aux = l
            else:
                aux = '*'
            frase = frase + aux
        if frase == palavra:
            print('Voce ganhou o Jogo!!!!!!')
            break
        print(f'A palavra está assim: {frase}')
    else:
        print(f'A letra {letra} não está na palavra. Tente novamente!')
        continue
        if vidas > 0: #Verificar se ainda temos vidas
            vidas -= 1
        if vidas == 0:
            print('Voce perdeu o jogo.')
            print(f'A palavra-chave era: {palavra}')
            break
        print(f'Agora você tem um total de {vidas} tentativa(s).\n')
    print(f'As palavras letras que ja fora usadas são: {letras_usadas}')
print('Jogo finalizado...')


    #monstrar



#Iniciar o processo repetivo de tentativas, se ainda restam vidas ou não