#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

c1 = float(input('Digite o um dos catetos: '))
c2 = float(input('Digite o outro cateto: '))

h = hypot(c1,c2)

print('A hipotenusa de um triângulo de catetos {} e {} é {:.2f}'.format(c1,c2,h))