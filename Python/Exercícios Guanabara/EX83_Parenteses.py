#recebe uma expressão de parênteses
#define se a expressão está balanceada

exp = str(input("digite a expressao: "))
lista=[]
aux=0

for i in exp:
    if i=='(':
        lista.append('(')
    elif i==')' and len(lista)==0:
        print("desbalanceado")
        aux=1
        break
    elif i==')':
        lista.pop()
if len(lista)==0 and aux==0:
    print("ok")
elif len(lista)!=0 and aux==0:
    print("nao ok")