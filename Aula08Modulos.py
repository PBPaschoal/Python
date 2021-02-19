#Aula08 Exercicio 01 (na verdade é 016 do) Curso em Vídeo Python
#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exemplo: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

import math
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))

'''Ou
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))'''


'''Ou
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''