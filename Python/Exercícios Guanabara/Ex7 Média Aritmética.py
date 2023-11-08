#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
n1=float(input('qual foi a primeira nota do aluno? '))
n2=float(input('qual foi a segunda nota do aluno? '))
ma =(n1+n2)/2
print('considerando que a primeira nota do aluno foi {} e a segunda nota foi {}, a média aritmética do aluno é {}.'.format(n1, n2, ma))

n1=float(input('qual foi a primeira nota do aluno? '))
n2=float(input('qual foi a segunda nota do aluno? '))
print('considerando que a primeira nota do aluno foi {} e a segunda nota foi {}, a média aritmética do aluno é {}.'.format(n1, n2, (n1+n2)/2))

#caso haja uma necessidade do número quebrado só ter um número após a vírgula, na média, dentro da chave coloca ":.1f" - que significa que só precisa de uma flutuante, após o número inteiro. dessa forma, há um arredondamento do resultado.
n1=float(input('qual foi a primeira nota do aluno? '))
n2=float(input('qual foi a segunda nota do aluno? '))
print('considerando que a primeira nota do aluno foi {} e a segunda nota foi {}, a média aritmética do aluno é {:.1f}.'.format(n1, n2, (n1+n2)/2))
