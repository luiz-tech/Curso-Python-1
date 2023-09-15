#Faça um algoritmo que leia o salário de um funcionário e mostre
#seu novo salário, com 15% de aumento.

salario = float(input('Informe o salario atual: '))

salario = salario + (salario * 0.15)

print('O salario com reajuste é R$ {:.2f}'.format(salario))