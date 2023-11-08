#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9:RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
média=(n1+n2)/2
if média>=7:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {} \n O aluno está APROVADO!'.format(n1,n2,média))
elif média<5:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {} \n O aluno está REPROVADO!'.format(n1,n2,média))
else:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {} \n O aluno está em RECUPERAÇÃO!'.format(n1,n2,média))

