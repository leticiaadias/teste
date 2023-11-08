#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
 
casa=float(input("Valor da casa: R$ "))
salario=float(input("Salário do comprador: R$ "))
anos=int(input("Quantos anos de financiamento? "))
prestação=casa/(anos*12)
if prestação<0.30*salario:
    print('para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}, então o empréstimo pode ser CONCEDIDO!'.format(casa,anos,prestação))
else:    
    print('para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}, então o empréstimo foi NEGADO!'.format(casa,anos,prestação))
