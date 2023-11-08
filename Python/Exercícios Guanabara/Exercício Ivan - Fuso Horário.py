#Paulo e Pedro fizeram uma longa jornada desde que partiram do Brasil para competir na Final Mundial da Maratona, em Phuket, Tailândia.
#Notaram que a cada escala que faziam, tinham que ajustar seus relógios por causa do fuso horário.
#Assim, para melhor se organizarem para as próximas viagens, eles pediram que você faça um aplicativo para celular que:
#dada a hora de saída, tempo de viagem e o fuso do destino com relação à origem, calcule e informe a hora de chegada do vôo no destino.
#Por exemplo, se eles partiram às 10 horas da manhã para uma viagem de 4 horas rumo a um destino que fica a leste em um fuso horário com uma hora a mais com relação ao fuso horário do ponto de partida, a hora de chegada terá que ser: 10 horas + 4 horas de viagem + 1 hora de deslocamento pelo fuso, ou seja, chegarão às 15 horas no horário do destino.
#Note que se a hora calculada for igual a 24, seu programa deverá imprimir 0.

from datetime import datetime, timezone
hs=datetime(input('qual o horário de saída? '))
tv=datetime(input('qual o tempo de viagem? '))
fuso=timezone(input('qual o fuso horário? '))
h=hs+tv+fuso
if h==24:
    input('o horário é: 00:00h')
else:
    input('o horário é {::2f}h'.format(h))
