#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#calcule e mostre o comprimento da hipotenusa.

co=float(input('digite o comprimento do cateto oposto: '))
ca=float(input('digite o comprimenot do cateto adjacente: '))
h=(co**2+ca**2)**(1/2)
print('a hipotensa vai medir {:.2f}'.format(h))

import math 
co=float(input('digite o comprimento do cateto oposto: '))
ca=float(input('digite o comprimenot do cateto adjacente: '))
h= math.hypot(co,ca)
print('a hipotensa vai medir {:.2f}'.format(h))
