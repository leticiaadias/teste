#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao=str(input('Digite a expressão: '))
lista=[]
for simbolo in expressao:
    if simbolo=='(':
        lista.append('(')
    elif simbolo==')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista)==0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
    