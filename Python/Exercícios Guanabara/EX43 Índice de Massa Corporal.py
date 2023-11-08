#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso;
# Entre 18.5 e 25: Peso normal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade;
# Acima de 40: Obesidade mórbida.

peso=float(input('Qual o seu peso? (Kg) '))
altura=float(input('Qual é a sua altura? (m) '))
IMC=peso/(altura*altura)
if IMC<18.5:
    print('O IMC desssa pessoa é de {:.2F} \n Você está ABAIXO DO PESO normal'.format(IMC))
elif IMC>=18.5 and IMC<25:
    print('O IMC desssa pessoa é de {:.2F} \n PARABÉNS, você está na faixa de PESO NORMAL.'.format(IMC))
elif IMC>=25 and IMC<30:
    print('O IMC desssa pessoa é de {:.2F} \n Você está em SOBREPESO'.format(IMC))
elif IMC>=30 and IMC<40:
    print('O IMC desssa pessoa é de {:.2F} \n Você está em OBESIDADE!'.format(IMC))
else:
    print('O IMC desssa pessoa é de {:.2F} \n Você está em OBESIDADE MÓRBIDA, cuidado!'.format(IMC))
