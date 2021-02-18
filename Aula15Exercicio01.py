#Aula15 Exercicio 01 (na verdade 015 total) Curso em Vídeo Python
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15
#por Km rodado.
dias = int(input('Informe quantos dias deseja alugar o carro: '))
km01 = float(input('Informe a quantidade de KM percorridos: '))
valortotal = (dias * 60) + (km01 * 0.15)
print('Total a pagar: R$ {:.2f}'.format(valortotal))
