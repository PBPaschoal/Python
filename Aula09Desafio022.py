#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas minúsculas.
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome.

nome = str(input('Informe o seu nome completo: ')).strip() #eliminando os espaços antes e depois.
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #eliminando os espaços durante.
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
