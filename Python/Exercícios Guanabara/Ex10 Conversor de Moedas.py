#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considere US$1,00 = R$3,27
r=float(input('quantos reais você tem na carteira? R$ '))
d=r/3.27
print('considerando que você tem R$ {:.2f} na sua carteira, dessa forma, você tem US${:.2f}.'.format(r,d))
