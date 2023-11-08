#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
#Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador=randint(0,5)
jogador=int(input('Em que número eu pensei? '))
if (jogador==computador):
    print ('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador,jogador))
