#Desenvolva um programa que leia as duas notas de
#um aluno, calcule e mostre a sua média.

n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))

m = (n1 + n2)/2

print('1º BIM {}\n2º BIM {}\n\nMédia {:.1f}'.format(n1,n2,m))

