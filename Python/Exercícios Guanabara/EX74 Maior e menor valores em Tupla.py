#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
n1=randint(1,10)
n2=randint(1,10)
n3=randint(1,10)
n4=randint(1,10)
n5=randint(1,10)
tupla=(n1,n2,n3,n4,n5)
print(f'Valores sorteados foram: {tupla}')
maior=0
menor=11
if n1>maior:
    maior=n1
if n2>maior:
    maior=n2
if n3>maior:
    maior=n3
if n4>maior:
    maior=n4
if n5>maior:
    maior=n5
if n1<menor:
    menor=n1
if n2<menor:
    menor=n2
if n3<menor:
    menor=n3
if n4<menor:
    menor=n4
if n5<menor:
    menor=n5
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')


from random import randint
numeros=(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')


from random import randint
numeros=(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
maior=0
menor=11
for i in range(0,len(numeros)):
    if numeros[i]>maior:
        maior=numeros[i]
    if numeros[i]<menor:
        menor=numeros[i]
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')