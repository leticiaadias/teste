#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

lista=[]
pares=[]
impares=[]
while True:
    lista.append(int(input('Digite um número: ')))
    resp=str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'Nn':
        break
for n in lista:
    if n%2==0:
        pares.append(n)
    elif n%2==1:
        impares.append(n)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista com os valores pares é {pares}')
print(f'A lista com os valores ímpares é {impares}')
