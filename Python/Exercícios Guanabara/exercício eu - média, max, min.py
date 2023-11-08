#Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota

n1=float(input('primeira nota: '))
n2=float(input('segunda nota: '))
n3=float(input('terceira nota: '))
n4=float(input('quarta nota: '))
lista=[n1,n2,n3,n4]
print('a média é: {:.2f}, a maior nota é: {:.2f} e a menor nota é: {:.2f}'.format((n1+n2+n3+n4)/4,max(lista), min(lista)))

n1=float(input('primeira nota: '))
n2=float(input('segunda nota: '))
n3=float(input('terceira nota: '))
n4=float(input('quarta nota: '))
lista=[n1,n2,n3,n4]
print('a média é: {:.2f}, a maior nota é: {:.2f} e a menor nota é: {:.2f}'.format((sum(lista)/4),max(lista), min(lista)))
