# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep
itens=('pedra','papel','tesoura')
computador=randint(0,2)
jogador=int(input("""Suas opções:  
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? """))
print(' JO')
sleep(1)
print(' KEN')
sleep(1)
print(' PÔ')
sleep(1)     
print(' -=-=-=-=-=-=-=-=-=-=-=-= \n Computador jogou {} \n jogador jogou {} \n -=-=-=-=-=-=-=-=-=-=-=-='.format(itens[computador],itens[jogador]))

if computador==0 and jogador==2 or computador==1 and jogador==0 or computador==2 and jogador==1:
    print(' Computador Ganhou!!!')
elif jogador==0 and computador==2 or jogador==1 and computador==0 or jogador==2 and computador==1:
    print(' Jogador Ganhou!!!')
elif computador==jogador:
    print(' Empate!!!')
    