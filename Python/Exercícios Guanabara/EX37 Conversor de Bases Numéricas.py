#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

n=int(input('Digite um número inteiro: '))
conversao=int(input('[ 1 ] converter para BINÁRIO \n [ 2 ] converter para OCTAL \n [ 3 ] converter para HEXADECIMAL \n Sua opção: '))
if conversao==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)))
elif conversao==2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)))
elif conversao==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)))
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
