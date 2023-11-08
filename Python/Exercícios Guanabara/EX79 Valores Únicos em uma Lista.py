#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

listanum=[]
while True:
    n=(int(input('Digite um valor: ')))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    resp=str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in'Nn':
        break
print('-='*30)
listanum.sort()
print(f'Você digitou os valores: {listanum}')
