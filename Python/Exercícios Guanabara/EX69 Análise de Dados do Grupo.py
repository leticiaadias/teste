#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

dezoitoanos=homens=mulheres=0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade=int(input('Idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade>=18:
        dezoitoanos+=1
    if sexo=='M':
        homens+=1
    if sexo=='F' and idade<20:
        mulheres+=1
    print('-'*20)
    continuar=' '
    while continuar not in 'SN':
        continuar=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar=='N':
        break
print('-'*20)
print (f'Total de pessoas com mais de 18 anos: {dezoitoanos}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
