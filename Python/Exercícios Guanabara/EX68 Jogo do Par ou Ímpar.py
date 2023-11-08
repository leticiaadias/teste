#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
ganhou=0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador=int(input('Diga um valor: '))
    computador=randint(0,10)
    total=computador+jogador
    poui=' '
    while poui not in 'PI':
        poui=str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
        print('-'*20)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}',end='')
    print(' DEU PAR' if total%2==0 else ' DEU ÍMPAR')
    if poui== 'P':
        if total%2==0:
            print('Você VENCEU!')
            ganhou+=1
        else:
            print('Você PERDEU!')
            break
    elif poui== 'I':
        if total%2==1:
            print('Você VENCEU!')
            ganhou+=1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print ('-'*20)
print(f'GAME OVER! Você vendeu {ganhou} vezes.')
print('-'*20)
