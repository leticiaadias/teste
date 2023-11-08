#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA')
print('-='*10)
primeirotermo=int(input('informe o primeiro termo da PA: '))
razao=int(input('Informe a razão da PA: '))
termo=primeirotermo
cont=1
total=0
mais=10
print('Os 10 primeiros termos da PA que tem com primeiro termo {} e razão {}, são: ' .format(primeirotermo,razao))
while mais!=0:
    total+=mais    
    while cont<=total:
        print('{} - ' .format(termo),end='')
        termo+=razao
        cont+=1
    print('PAUSA')
    mais= int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.' .format(total))
