#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SêNIOR
# Acima: MASTER

from datetime import date
atual=date.today().year
nascimento=int(input('Ano de nascimento: '))
idade=atual-nascimento
if idade<=9:
    print('O atleta tem {} anos. \n Classificação: MIRIM'.format(idade))
elif idade<=14:
    print('O atleta tem {} anos. \n Classificação: INFANTIL'.format(idade))
elif idade<=19:
    print('O atleta tem {} anos. \n Classificação: JÚNIOR'.format(idade))
elif idade<=25:
    print('O atleta tem {} anos. \n Classificação: SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos. \n Classificação: MASTER'.format(idade))
