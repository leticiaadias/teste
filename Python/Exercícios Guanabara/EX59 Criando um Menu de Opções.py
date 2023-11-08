#Crie um programa que leia dois valores e mostre um menu como o abaixo.
#Seu programa deverá realizar a operação solicitada em cada caso.
#[ 1 ] Somar
#[ 2 ] Multiplicar
#[ 3 ] Maior
#[ 4 ] Novos números
#[ 5 ] Sair do programa


valor1=float(input('Digite um valor: '))
valor2=float(input('Digite outro valor: '))
opcao=0
while opcao != 5:
    opcao=int(input('[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa \n >>>>> Qual é a sua opção? ')) 
    if opcao==1:
        print('A soma entre {} + {} é {}' .format(valor1,valor2,valor1+valor2))
    elif opcao==2:
       print ('O resultado de {} x {} é {}' .format(valor1,valor2,valor1*valor2))
    elif opcao==3:
        if valor1>valor2:
            maior=valor1
        else:
            maior=valor2
            print('Entre {} e {} o maior valor é {}' .format(valor1,valor2,maior))
    elif opcao==4:
        print('informe novos números!')
        valor1=float(input('Digite um valor: '))
        valor2=float(input('Digite outro valor: '))
    elif opcao==5:
        print('Fim do programa. Volte sempre!')
    else:
        print('Opção inválida, tente novamente!')

