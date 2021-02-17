#Aula07 Exercicio Curso em Vídeo Python
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Preço do produto R$'))
novopreco = preco - (preco * 5 / 100)
print('Com 5% de desconto o novo preço é R${:.2f}'.format(novopreco))
