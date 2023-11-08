#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#EX.: digite um número: 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1

num=int(input('Informe um número: '))
n=str(num)
print('Analisando o número {}'.format(n))
print('unidade: {}'.format(n[3]))
print('dezena: {}'.format(n[2]))
print('centena: {}'.format(n[1]))
print('milhar: {}'.format(n[0]))

num=int(input('Informe um número: '))
u=num/1%10
d=num/10%10
c=num/100%10
m=num/1000%10
print('Analisando o número {}'.format(n))
print('unidade: {:.0f}'.format(u))
print('dezena: {:.0f}'.format(d))
print('centena: {:.0f}'.format(c))
print('milhar: {:.0f}'.format(m))
