#Crie um porgrama que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)

s=cont=0
while n!=999:
    n=int(input('Digite um valor (999 para parar): '))
    if n==999:
        break
    cont+=1
    s+=n
print(f'Foram digitados {cont} números e a soma entre eles é {s}')
