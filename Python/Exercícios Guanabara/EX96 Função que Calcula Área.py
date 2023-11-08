#Faça um programa que tenha uma função chamada área()
#que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg,comp):
    a=larg*comp
    print(f'A área de um terreono {larg} X {comp} é de {a}m²')


#programa principal
print('Controle de terrenos')
print('-'*20)
l=float(input('LARGURA(m): '))
c=float(input('COMPRIMENTO(m): '))
area(l,c)
