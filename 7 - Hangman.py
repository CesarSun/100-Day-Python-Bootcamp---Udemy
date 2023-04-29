from faker import Faker
import random


fake = Faker('pt_BR')

palavra = fake.word()

letras_adivinhadas = ['_'] * len(palavra)

tentativas_maximas = 6
tentativas = 0
letras_incorretas = []

print('Vamos jogar Hangman!')


def desenhar_boneco_enforcado(erros, letras_incorretas):
    if erros == 0:
        print(' +---+')
        print(' |   |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('Erros', letras_incorretas)
    elif erros == 1:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('     |')
        print('     |')
        print('     |')
        print('Erros', letras_incorretas)
    elif erros == 2:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print(' |   |')
        print('     |')
        print('     |')
        print('Erros', letras_incorretas)
    elif erros == 3:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|   |')
        print('     |')
        print('     |')
        print('Erros', letras_incorretas)
    elif erros == 4:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('     |')
        print('     |')
        print('Erros', letras_incorretas)
    elif erros == 5:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/    |')
        print('     |')
        print('Erros', letras_incorretas)
    elif erros == 6:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/ \  |')
        print('     |')
    else:
        print('Número de erros inválido.')

erros = 0

while True:
    desenhar_boneco_enforcado(erros=erros, letras_incorretas=letras_incorretas)
    print(' '.join(letras_adivinhadas))
    letra = input('Digite uma letra: ').lower()
    
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_adivinhadas[i] = letra
    else:
        letras_incorretas.append(letra)
        tentativas += 1
        erros += 1
        print('Letra incorreta.')
        
    if '_' not in letras_adivinhadas:
        print('Parabéns! Você adivinhou a palavra {}.'.format(palavra))
        break
    
    if tentativas == tentativas_maximas:
        desenhar_boneco_enforcado(erros=erros, letras_incorretas=letras_incorretas)
        print('Game over! A palavra era {}.'.format(palavra))
        break