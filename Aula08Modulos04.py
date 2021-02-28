#Aula08 Exercicio 04 (na verdade é o 019 do) Curso em Vídeo Python
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido.
import random
aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')
print('O aluno escolhido foi: {}.'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))


#Ou
#import random
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Segundo aluno: '))
#n3 = str(input('Terceiro aluno: '))
#n4 = str(input('Quarto aluno: '))
#lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista)
#print('O aluno escolhido foi {}'.format(escolhido))

#Ou
#from random import choice
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Segundo aluno: '))
#n3 = str(input('Terceiro aluno: '))
#n4 = str(input('Quarto aluno: '))
#lista = [n1, n2, n3, n4]
#escolhido = choice(lista)
#print('O aluno escolhido foi {}'.format(escolhido))