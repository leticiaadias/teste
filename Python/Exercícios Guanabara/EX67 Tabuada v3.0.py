#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    if n<0:
        break
    print('-'*20)
    print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(n,n*1,n,n*2,n,n*3,n,n*4,n,n*5,n,n*6,n,n*7,n,n*8,n,n*9,n,n*10,))
    print('-'*20)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')

while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    if n<0:
        break
    print('-'*20)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*20)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
