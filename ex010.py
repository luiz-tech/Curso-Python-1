#Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Informe o valor em reais: '))
cotacao = float(input('Informe a cotação de hoje: '))

dolar = real / cotacao

print('{:.2f} reais valem {:.2f} na cotação oficial de hoje'.format(real,dolar))

