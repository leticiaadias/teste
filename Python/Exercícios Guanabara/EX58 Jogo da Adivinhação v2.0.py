#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador=randint(0,10)
print('Sou seu computador... acabei de pensar em u número entre 0 e 10. \nSerá que você consegue adivinhar qual foi? ')
acertou= False
palpites=0
while not acertou:
    jogador=int(input('Qual é o seu palpite? '))
    palpites+=1
    if jogador==computador:
        acertou= True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Você conseguiu me vencer com {} palpites' .format(palpites))
