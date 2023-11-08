#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo sem considerar espaços;
#Quantas letras tem o primeiro nome.

nome=str(input('Digite seu nome completo: ')).strip()
maiusculas=nome.upper()
minusculas=nome.lower()
letras=len(nome)-nome.count(' ')
separa=nome.split()
primeiron=separa[0]
primeiro=nome.find(' ')
print("""Analisando seu nome...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras""".format(maiusculas,minusculas,letras,primeiron,primeiro))

nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa=nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
