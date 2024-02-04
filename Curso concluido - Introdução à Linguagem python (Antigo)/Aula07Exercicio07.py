#Aula07 Exercicio Curso em Vídeo Python
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
