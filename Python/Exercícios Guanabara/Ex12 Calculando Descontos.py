#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço=float(input('qual o preço do produto? R$ '))
desc=(preço*5)/100
preçofinal = preço-desc
print('o preço do produto é R${:.2f}, com o desconto de 5% de {:.2f}, o preço passa a ser R${:.2f}.'.format(preço,desc,preçofinal))
