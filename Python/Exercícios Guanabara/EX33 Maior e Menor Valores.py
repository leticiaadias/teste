#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
n3=int(input('Digite o terceiro valor: '))
if n1<n2 and n1<n3:
    print('O menor valor digitado foi: {}'.format(n1))
elif n2<n1 and n2<n3:
    print('O menor valor digitado foi: {}'.format(n2))
else:
    print('O menor valor digitado foi: {}'.format(n3))
if n1>n2 and n1>n3:
    print('O maior valor digitado foi {}'.format(n1))
elif n2>n1 and n2>n3:
    print('O maior valor digitado foi: {}'.format(n2))
else:
    print('O maior valor digitado foi: {}'.format(n3))

n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
n3=int(input('Digite o terceiro valor: '))
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
