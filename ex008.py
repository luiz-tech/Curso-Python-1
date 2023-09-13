#Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

m = float(input('Informe o valor em metros'))

mm = m * 1000
cm = m * 100

print('O valor em milimetros é {} e em centimetros é {}'.format(mm,cm))