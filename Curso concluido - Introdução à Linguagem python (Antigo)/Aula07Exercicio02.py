#Aula07 Exercicio Curso em Vídeo Python
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Informe um número: '))
print('O dobro de {} vale: {}'.format(numero, (numero*2)))
print('O triplo de {} vale: {}. \nA raiz quadrada de {} vale: {:.2f}.'.format(numero, (numero*3), numero, pow(numero, (1/2))))


