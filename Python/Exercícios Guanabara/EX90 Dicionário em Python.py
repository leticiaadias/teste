#Faça um programa que leia nome e média de um aluno, guardando a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

aluno=dict()
aluno['nome']=str(input('Nome: '))
aluno['média']=float(input(f'Média de {aluno["nome"]}: '))
if aluno['média']>=7:
    aluno['situação'] = 'APROVADO'
elif 5<=aluno['média']<7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('-='*15)
for k, v in aluno.items():
    print (f'- {k}: {v}')
