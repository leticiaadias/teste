#Refaça o DESAFIO 009, mostrando a tabuada de um npumero que o usuário escolher;
#Só que agora utilizando um LAÇO FOR.

n=int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print('{} x {} = {}'.format(n,c,n*c))
