#fazer um programa que calcule o valor final do produto e discrimine na nota fiscal quanto o cliente pagou em:
#impostos (Imposto de importação e ICMS), frete e total a pagar.
#segue algumas informações que você precisará saber para resolver essa questão:
#a taxa de importação para eletrônicos é de 60%;
#o calculo do ICMS é dado pela formula: (Valor Final do produto x Aliquota)
#o valor final do produto é dado pela soma do (Valor do Produto + Frete + Impostos de Importação) / (1 - Aliquota)
#a empresa tem a cultura de não adicionar o frete no cálculo, para valores de US$ 2,500 em diante. Informe isso ao fim da nota.
dólar=float(input('informe o valor do dólar: '))
vpd=float(input('informe o valor do produto em dólar: '))
aliquota1=float(input('informa a porcentagem da aliquota: '))
frete=float(input('informe o valor do frete em dólar: '))
print('a cotação do dólar é de R${:.2f}, o valor do produto é de: U${:.2f}, o percentual da alíquota do ICMS é de: {}% e o valor do frete é de: U${:.2f}.'.format(dólar,vpd,aliquota1,frete))
vpr=vpd*dólar
freter=frete*dólar
aliquota2=aliquota1/100
importação=(vpr*60)/100
vf=(vpr+importação)/(1-aliquota2)
icms=vf*aliquota2
vf=vf+icms
if(vpd<2500):
    vf=vf+freter
print('O valor do produto é de: R${:.2f}, o icms é R${:.2f} e o valor total a pagar é de: R${:.2f}'.format(vpr,icms,vf))



#impostos=(vp*60)/100
#if(vf>2500):
#    frete=0
#else:
#   frete=100
#vf=(vp+frete+impostos) / (1-aliquota)
#icms=vf*aliquota