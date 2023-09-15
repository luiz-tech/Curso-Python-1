#Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada # litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))

area = largura * altura
litros = area / 2

print('Essa parede tem {:.2f} metros quadrados e demanda {:.2f}L de tinta'.format(area,litros))