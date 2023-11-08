#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
genero=int(input('Qual é o seu gênero? \n [ 1 ] Feminino \n [ 2 ] Masculino \n'))
if genero==1:
    print ('Você não precisa se alistar!')

else:
    atual= date.today().year
    nascimento=int(input('Ano de nascimento: '))
    idade=atual-nascimento
    if idade<18:
        print('Quem nasceu em {} tem {} anos em 2023. \n Ainda faltam {} anos para o alistamento. \n Seu alistamento será em {}!'.format(nascimento,idade,18-idade,nascimento+18))
    elif idade==18:
        print('Quem nasceu em {} tem {} anos em 2023. \n Você tem que se alistar IMEDIATAMENTE!'.format(nascimento,idade))
    elif idade>18:
        print('Quem nasceu em {} tem {} anos em 2023. \n Você já deveria ter se alistado há {} anos. Seu alistamento foi em {}!'.format(nascimento,idade,idade-18,nascimento+18))
