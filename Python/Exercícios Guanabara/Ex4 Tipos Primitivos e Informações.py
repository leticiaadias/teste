#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a=input('digite algo.')
print('o tipo primitivo desse valor é', type(a))
print('só tem espaços?', a.isspace())
print('é um número?', a.isnumeric())
print('é alfabético?', a.isalpha())
print('é alfanumérico?', a.isalnum())
print('é maiúsculo?', a.isupper())
print('é minúsculo?', a.islower())
print('está captalizada?', a.istitle())
