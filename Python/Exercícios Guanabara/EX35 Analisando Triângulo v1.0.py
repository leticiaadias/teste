#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário de elas podem ou não formar um triângulo.

r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))
if r1-r2<r3<r1+r2 and r1-r3<r2<r1+r3 and r2-r3<r1<r2+r3:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

#((|r1-r2|<r3) and (r3<r1+r2))
#if r1-r2<r3<r1+r2 or r1-r3<r2<r1+r3 or r2-r3<r1<r2+r3:
    #print('Os segmentos acima PODEM FORMAR triângulo!')
#else:
    #print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
