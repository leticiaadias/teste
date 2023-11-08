#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim=list()
while True:
    nome=str(input('Nome: '))
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    media=(n1+n2)/2
    boletim.append([nome, [n1,n2],media])
    resp=str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc=int(input('Quer mostrar a nota de qual aluno? (999 interrompe) '))
    if opc==999:
        print('FINALIZANDO...')
        break
    if opc<=len(boletim)-1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
