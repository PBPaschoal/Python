#Aula014 Exercicio Curso em Vídeo Python
#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
#Exercicio 014(01 da aula 14).
c = float(input('Informe a temperaduta em ºC: '))
f = 9 * c / 5 + 32 #f = ((9 * c) / 5) + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
