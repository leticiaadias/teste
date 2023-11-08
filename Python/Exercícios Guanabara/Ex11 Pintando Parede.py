#faça um programa que leia a largura e a altura de uma parede em metros;
#calcule a sua área e a quantidade de tinta necessária para pintá-la.
#info: cada litro de tinta pinta uma área de 2m².

larg=float(input('qual a largura da parede? '))
alt=float(input('qual a altura da parede? '))
área=larg*alt
litros=área/2
print('área da parede é de {}m², portanto, são necessários {} litros de tinta para pintá-la.'.format(área,litros))
