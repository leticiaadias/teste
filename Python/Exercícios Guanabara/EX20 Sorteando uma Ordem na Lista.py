#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1=input('primeiro aluno: ')
a2=input('segundo aluno: ')
a3=input('terceiro aluno: ')
a4=input('quarto aluno: ')
lista=[a1,a2,a3,a4]
ordem=shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

import random
a1=input('primeiro aluno: ')
a2=input('segundo aluno: ')
a3=input('terceiro aluno: ')
a4=input('quarto aluno: ')
lista=[a1,a2,a3,a4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

#primeiro aluno:
#segundo aluno:
#terceiro aluno:
#quarto aluno:
#A ordem de apresentação será: 