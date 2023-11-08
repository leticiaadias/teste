#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
 
salario=float(input('Qual o salário do funcionário? R$ '))
if salario<=1250:
    aumento=salario*0.15
    salario1=salario+aumento
else:
    aumento=salario*0.10
    salario1=salario+aumento
print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora'.format(salario,salario1))

salario=float(input('Qual o salário do funcionário? R$ '))
if salario<=1250:
    aumento=salario+(salario*0.15)
else:
    aumento=salario+(salario*0.10)
print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora'.format(salario,aumento))
