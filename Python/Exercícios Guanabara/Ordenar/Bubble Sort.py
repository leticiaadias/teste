#dê três números em ordem crescente
n1=input('dê um número: ')
n2=input('dê um número: ')
n3=input('dê um número: ')
n4=input('dê um número: ')
if(n1>n2):
    aux=n1
    n1=n2
    n2=aux
if(n1>n3):
    aux=n1
    n1=n3
    n3=aux
if(n1>n4):
    aux=n1
    n1=n4
    n4=aux
if(n2>n3):
    aux=n2
    n2=n3
    n3=aux
if(n2>n4):
    aux=n2
    n2=n4
    n4=aux
if(n3>n4):
    aux=n3
    n3=n4
    n4=aux
print(n1,n2,n3,n4)

if(n1<=n2 and n1<=n3):
    print(n1)
elif(n2<=n1 and n2<=n3):
    print(n2)
elif(n3<=n1 and n3<=n2):
    print(n3)
if((n1<=n2 and n1>=n3) or (n1>=n2 and n1<=n3)):
    print(n1)
elif((n2<=n1 and n2>=n3) or (n2>=n1 and n2<=n3)):
    print(n2)
elif((n3<=n1 and n3>=n2) or (n3>=n1 and n3<=n2)):
    print(n3)
if(n1>=n2 and n1>=n3):
    print(n1)
elif(n2>=n1 and n2>=n3):
    print(n2)
elif(n3>=n1 and n3>=n2):
    print(n3)
