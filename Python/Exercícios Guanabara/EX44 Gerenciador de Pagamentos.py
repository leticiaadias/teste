# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: preço normal;
# 3X ou mais no cartão: 20% de juros.

preço=float(input('Preço das compras: R$ '))
pagamento=int(input("""[ 1 ] à vista dinheiro/cheque \n [ 2 ] à vista cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão \n Qual é a opação? """))
if pagamento==1:
    desconto=preço*0.10
    print ('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(preço,preço-desconto))
elif pagamento==2:
    desconto=preço*0.05
    print ('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(preço,preço-desconto))
elif pagamento==3:
    parcelas=int(input('Quantas parcelas? '))
    vp=preço/parcelas
    print ('Sua compra será parcelada em {}x de R${:.2f}. \n Sua compra vai custar {:.2f} no final'.format(parcelas,vp,preço))
elif  pagamento==4:
    parcelas=int(input('Quantas parcelas? '))
    juros=preço*0.20
    print ('Sua compra será parcelada em {}x de R${:.2f} COM JUROS. \n Sua compra de {:.2f} vai custar {:.2f} no final.'.format(parcelas,(preço+juros)/parcelas,preço,preço+juros))
else:
    pagamento=0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
    