#Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# . Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado.

km = float(input('Informe quantos km(s) foram percorridos: '))
d = int(input('Quantos dias o carro ficou alugado ? '))

soma = ( km * 0.15 ) + ( d * 60 )

print('O preço final do alguem foi de R$ {:.2f}'.format(soma))