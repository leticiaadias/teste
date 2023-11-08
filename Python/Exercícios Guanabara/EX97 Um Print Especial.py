#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#OBS.: OLHAR O EXEMPLO NO VÍDEO

def escreva(msg):
    tam=len(msg) +4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

    
#programa princial
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
