#escreva um programa que pergunte a quantidade de Km percorridos por um carro de aluguel
#e a quantidade de dias pelos queias ele foi alugado.
#calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km=float(input('quantos km foram percorridos? '))
dias=int(input('quantos dias o carro foi alugado? '))
vc=dias*60
vk=km*0.15
vp=float(vc+vk)
print('o valor a pagar é de R${:.2f}'.format(vp))
