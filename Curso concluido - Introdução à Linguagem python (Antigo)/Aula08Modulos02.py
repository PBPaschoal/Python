#Aula08 Exercicio 02 (na verdade é o 017 do) Curso em Vídeo Python
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#retangulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

'''Ou
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
