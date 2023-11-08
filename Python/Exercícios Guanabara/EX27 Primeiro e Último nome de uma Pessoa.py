#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#EX.: Ana Maria de Souza
#primeiro: Ana
#último: Souza

nome=str(input('Digite o nome completo: '))
print(nome.split)


















n=str(input('Digite seu nome completo: ')).strip()
nome=n.split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O último nome é: {}'.format(nome[len(nome)-1]))
