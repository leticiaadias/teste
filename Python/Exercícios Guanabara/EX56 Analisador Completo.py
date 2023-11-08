#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#A média de idade do grupo;
#Qual é o nome do homem mais velho;
#Quantas mulheres tem menos de 20 anos.

somaidade=0
media=0
maiorhomem=0
nomevelho=0
mulher20=0
for pessoa in range(1,5):
    nome=str(input('----- {}ª PESSOA ----- \nNome: '.format(pessoa))).strip()
    idade=int(input('Idade: '))
    sexo=str(input('[M/F]: ')).strip().upper()
    somaidade+=idade
    media=somaidade/4
    if pessoa==1 and sexo=='M':
        maiorhomem=idade
        nomevelho=nome
    if sexo=='M' and idade>maiorhomem:
        maiorhomem=idade
        homemvelho=nome
    if sexo=='F' and idade<20:
        mulher20+=1
print('A média de idade do grupo é de {} anos' .format(media))
print('O homem mais velho tem {} anos e se chama {}' .format(maiorhomem,homemvelho))
print('Ao todo são {} mulher com menos de 20 anos' .format(mulher20))
