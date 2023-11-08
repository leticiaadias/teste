n1 = int(input('me dê um valor: '))
n2 = int(input('me dê outro valor: '))
soma = n1 + n2
if (n1>n2):
    sub=n1-n2
else:
    sub=n2-n1
multi = n1*n2
if (n1>n2):
    div=n1/n2
else:
    div=n2/n1
exp = n1**n2
print ('a soma é: {}, a sub é: {}, a multi é: {}, a div é: {} e a exp é: {}.' .format(soma,sub,multi,div,exp))
