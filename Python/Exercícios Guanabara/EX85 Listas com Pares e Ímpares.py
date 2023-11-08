#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única.
#Mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

numeros=[[],[]]
valor=0
for c in range(0,7):
    valor= int(input(f'Digite o {c+1}º valor: '))
    if valor%2==0:
        numeros[0].append(valor)
    elif valor%2==1:
        numeros[1].append(valor)
print('-='*40)
numeros[0].sort()
numeros[1].sort()
print (f'Os valores pares digitados foram: {numeros[0]}')
print (f'Os valores ímpares digitados foram: {numeros[1]}')
