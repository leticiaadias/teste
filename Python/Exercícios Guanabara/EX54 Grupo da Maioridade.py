#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
totalmaior=0
totalmenor=0
for pessoa in range(1,8):
    nasc=int(input('Em que ano a {}ª pessoa nasceu? '. format(pessoa)))
    atual=date.today().year
    idade=atual-nasc
    if idade >= 18:
        totalmaior=totalmaior+1
    else:
        totalmenor+=1
print('Ao todo tivemos {} pessoas maiores de idade' .format(totalmaior))
print('E também tivemos {} pessoas menores de idade' .format(totalmenor))



