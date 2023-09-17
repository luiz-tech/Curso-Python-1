# Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Informe o ângulo desejado: '))

sen = math.sin(angulo)
cos = math.cos(angulo)
tg = math.tan(angulo)

print(f'O seno de {angulo} é {sen}\nO cosseno de {angulo} é {cos}\nA tagente de {angulo} é {tg}')
