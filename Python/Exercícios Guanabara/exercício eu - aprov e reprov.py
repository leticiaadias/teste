#Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final.
#Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média.
#Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO".

n1=float(input('primeira nota: '))
n2=float(input('segunda nota: '))
n3=float(input('terceira nota: '))
n4=float(input('quarta nota: '))
lista=[n1,n2,n3,n4]
média=(n1+n2+n3+n4)/4
if (média>=7):
    input('APROVADO')
else:
    input('REPROVADO')
pf=float(input('digite a nota final: '))
mf=(média+pf)/2
if (mf>=5):
    input('APROVADO')
else:
    input('REPROVADO')
 