#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
tupla=('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
for pos in range(0, len(tupla)):
    if pos%2==0:
        print(f'{tupla[pos]:.<30}',end='')
    else:
        print(f'R$ {tupla[pos]:>6.2f}')
print('-'*40)
