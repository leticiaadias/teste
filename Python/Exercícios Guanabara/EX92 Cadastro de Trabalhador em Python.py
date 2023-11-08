#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CCTPS por diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
emprego=dict()
emprego['nome']= str(input('Nome: '))
nasc=int(input('Ano de Nascimento: '))
emprego['idade']= (date.today().year - nasc)
emprego['ctps']= int(input('Carteira de Trabalho (0 não tem): '))
if emprego['ctps'] != 0:
    emprego['ano de contratação']= int(input('Ano de Contratação: '))
    emprego['salário']= float(input('Salário: '))
    emprego['aposentadoria']= emprego['idade']+((emprego['ano de contratação']+35) - date.today().year)
print('-='*25)
for k, v in emprego.items():
    print(f'- {k} tem o valor {v}')
