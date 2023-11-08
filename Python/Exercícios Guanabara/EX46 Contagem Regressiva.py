#Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício, indo de 10 até 0. Com uma pausa de 1seg entre eles.

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("POW POW POW FOGOS FELIZ ANO NOVO")
