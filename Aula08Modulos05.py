#Aula08 Exercicio 05 (na verdade é o 020 do) Curso em Vídeo Python
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('Ordem de apresentação: ')
print(lista)

#Ou
#from random import shuffle
#aluno1 = str(input('Primeiro aluno: '))
#aluno2 = str(input('Segundo aluno: '))
#aluno3 = str(input('Terceiro aluno: '))
#aluno4 = str(input('Quarto aluno: '))
#lista = [aluno1, aluno2, aluno3, aluno4]
#shuffle(lista)
#print('Ordem de apresentação: ')
#print(lista)