#escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m=float(input('digite uma metragem: '))
km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000 
print('a distância de {} metros, corresponde a {}km, {}hm {}dam {}dm {}cm e {}mm.'.format(m,km,hm,dam,dm,cm,mm))

m=float(input('digite uma metragem: '))
print('a distância de {} metros, corresponde a {}km, {}hm {}dam {}dm {}cm e {}mm.'.format(m,m/1000,m/100,m/10,m*10,m*100,m*1000))
