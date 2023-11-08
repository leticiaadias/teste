#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n=int(input('digite um número: '))
d=n*2
t=n*3
rq=n**(1/2)
print('considerando o valor {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(n,d,t,rq))

n=int(input('digite um número: '))
print('considerando o valor {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(n,(n*2),(n*3),(n**(1/2))))
