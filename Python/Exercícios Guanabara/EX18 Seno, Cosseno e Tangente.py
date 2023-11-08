#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tngente desse ângulo.
import math
ang=float(input('digite um ângulo: '))
seno=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))
print=input('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang,seno))
print=input('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang,cos))
print=input('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang,tan))

import math
ang=float(input('digite um ângulo: '))
print=input('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang,math.sin(math.radians(ang))))
print=input('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang,math.cos(math.radians(ang))))
print=input('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang,math.tan(math.radians(ang))))

# O ânuglo de 30.0 tem o SENO de 0.50
# O ângulo de 30.0 tem o COSSENO de 0.87
# O ângulo de 30.0 tem a TANGENTE de 0.58