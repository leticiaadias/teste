#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n=cont=maior=menor=soma=media=0
resp='S'
while resp in'Ss':
    n=int(input('Digite um número: '))
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont+=1
    soma+=n
    media=soma/cont
    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
print('Você digitou {} números e a média foi {}\nO maior valor foi {} e o menor foi {}' .format(cont,media,maior,menor))
