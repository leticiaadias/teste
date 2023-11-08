#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa via informar quantas cédulas de cada valor serão entregues.
#OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*20,end='')
print('BANCO LELÊ',end='')
print('='*20)
valor=int(input('Qual valor você quer sacar? R$ '))
contced50=contced20=contced10=contced1=0
while valor>=50:
    contced50+=1
    valor-=50
if contced50>=1:
    print(f'O total de cédulas de R$50,00 reais é {contced50}')
while valor>=20:
    contced20+=1
    valor-=20
if contced20>=1:
    print(f'O total de cédulas de R$20,00 reais é {contced20}')
while valor>=10:
    contced10+=1
    valor-=10
if contced10>=1:
    print(f'O total de cédulas de R$10,00 reais é {contced10}')
while valor>=1:
    contced1+=1
    valor-=1
if contced1>=1:
    print(f'O total de cédulas de R$1,00 reais é {contced1}')
print('='*40)
print('Volte sempre ao BANCO LELÊ! Tenha um bom dia!')
