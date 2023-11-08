#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato e o seu valor.

tot=mais1000=barato=cont=soma=0
while True:
    produto=str(input('Nome do produto: '))
    preco=float(input('Valor do produto: $ '))
    continuar=str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
    cont+=1
    tot+=preco
print(f'O valor total gasto na compra foi de {soma}')
#total=produtos1000=menor=cont=0
#barato=''
#print('-'*20)
#print('LOJA SUPER BARATÃO')
#print('-'*20)
#while True:
    #produto=str(input('Nome do Produto: '))
    #preco=float(input('Preço: R$ '))
    #cont+=1
    #total+=preco
    #if preco>=1000:
        #produtos1000+=1
    #if cont==1 or preco<menor:
        #menor=preco
        #barato=produto
    #continuar=' '
    #while continuar not in 'SN':
        #continuar=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    #if continuar!='S':
        #break
#print('-'*10, end='')
#print(' FIM DO PROGRAMA ', end='')
#print('-'*10)
#print(f'O total da compra foi R${total:.2f}')
#print(f'Temos {produtos1000} produto(s) custando mais de R$1000,00')
#print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
