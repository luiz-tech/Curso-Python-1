# Exercício Python 006: Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número qualquer'))

d = n * 2
t = n * 3
r = pow(n,0.5)

print('O número {} possui como dobro {}, triplo {} e raiz quadrada {:.1f}'.format(n,d,t,r))

# a função pow() pode elevar um número ao quadrado tmb