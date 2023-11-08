#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
si=float(input('qual o salário? R$ '))
aumento=(si*15)/100
sf=si+aumento
print('o salário inicial era de R$ {:.2f}, com o desconto de 15% de R$ {:.2f}, o salário final passou a ser R$ {:.2f}'.format(si,aumento,sf))
