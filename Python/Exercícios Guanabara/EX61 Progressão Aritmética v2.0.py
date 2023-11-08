#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('-='*10)
primeirotermo=int(input('informe o primeiro termo da PA: '))
razao=int(input('Informe a razão da PA: '))
print('Os 10 primeiros termos da PA que tem com primeiro termo {} e razão {}, são: ' .format(primeirotermo,razao))
c=primeirotermo+razao
for c in range(primeirotermo,razao*11,razao):
    print('{}' .format(c),end=' - ')
print('FIM')



print('GERADOR DE PA')
print('-='*10)
primeirotermo=int(input('informe o primeiro termo da PA: '))
razao=int(input('Informe a razão da PA: '))
termo=primeirotermo
cont=1
print('Os 10 primeiros termos da PA que tem com primeiro termo {} e razão {}, são: ' .format(primeirotermo,razao))
while cont<=10:
    print('{} - ' .format(termo),end='')
    termo+=razao
    cont+=1
print('FIM')
