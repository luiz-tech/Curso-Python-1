#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
#primitivo e todas as informações possíveis sobre ele.

v = input("Digite algo")

print("O valor digitado é alfabético ? ", v.isalpha())
print("O valor digitado é numerico ? ", v.isnumeric())
print("O valor digitado é captalizado ? ", v.isupper())
print("O valor digitado é minúsiculo ? ", v.islower())


