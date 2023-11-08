#crie um programa que leia um número real qualquer pelo teclado.
#mostre na tela a sua porção inteira.
import math
nr=float(input('digite um valor: '))
ni= math.trunc(nr)
print('o valor digitado foi {} e a sua porção inteira é {}'.format(nr,ni))

import math
num=float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num,math.trunc(num)))

num=float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num,int(num)))
