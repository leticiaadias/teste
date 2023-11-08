#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

numeros=(int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores: ')
for n in numeros:
    print(f'{n}' ,end=' ')
cont=cont2=0
for n in numeros:
    if n==9:
        cont+=1
print(f'\nO numero 9 apareceu {cont} vezes')
for n in numeros:
    if n==3:
        print(f'O valor 3 apareceu na {(numeros.index(3)+1)}ª posição')
    if n%2==0:
        cont2+=1
print(f'Temos {cont2} valores pares')
