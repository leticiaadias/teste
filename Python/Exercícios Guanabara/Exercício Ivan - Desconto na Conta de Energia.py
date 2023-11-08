#A ELETROSHOCK S.A. é uma empresa de distribuição de energia bastante justa (pelo menos ela se diz ser!).
#Ela faz cobrança proporcional com a renda da família e o bairro.
#O programa deve imprimir uma mensagem de erro caso o bairro digitado seja inválido. OK
#Além disso, caso a renda da pessoa caia fora das faixas da tabela, não haverá desconto.
#Se a renda OU o consumo forem valores negativos, deve ser emitida uma mensagem de erro.
#O programa deve ler o código do bairro (S: Santa Ana; I: Industriários; T: Tabatinga);
#a renda da família e 

#----------------------------------------------------------------------------------------------

#ENTRADA
#Um caractere que indica o bairro do cliente ((S)anta Ana, (I)ndustriários, (T)abatinga)
#O valor da renda do usuário
#Seu consumo energético em reais

#SAÍDA
#Quanto a pessoa vai pagar já com o desconto.
#Caso a renda da pessoa caia fora das faixas da tabela, não haverá desconto.
#Mensagem de erro: Bairro invalido.
#Mensagem de erro: Renda e consumo nao podem ser negativos

bairro=input("digite o seu bairro: ")
if(bairro=='S'or bairro=='I'or bairro=='T'):
    renda=float(input('digite sua renda: '))
    consumo=float(input('digite o consumo em real: '))
    if(bairro=='S'):
        if ((renda>50.00 and renda<500.00)):
            desconto=50
            conta=consumo-desconto
            print('o valor da conta é de R$: {:.2f}'.format(conta))
        elif ((renda>=500.00 and renda<1000.00)):
            desconto=25
            conta=consumo-desconto
            print('o valor da conta é de R$: {:.2f}'.format(conta))
    elif(bairro=='I'):
        if ((renda>240.00 and renda<1000.00)):
            desconto=240
            conta=consumo-desconto
            print('o valor da conta é de R$: {:.2f}'.format(conta))
        elif ((renda>=1000 and renda<5000)):
            desconto=120
            conta=consumo-desconto
            print('o valor da conta é de R$: {:.2f}'.format(conta))
    elif(bairro=='T'):
        if ((renda>5000.00 and renda<10000.00)):
            desconto=720
            conta=consumo-desconto
            print('o valor da conta é de R$: {:.2f}'.format(conta))
        elif ((renda>10000.00 and renda<20000.00)):
            desconto=360
            conta=consumo-desconto
            print('o valor da conta é de R$: {:.2f}'.format(conta))
else:
     print("bairro invalido")
