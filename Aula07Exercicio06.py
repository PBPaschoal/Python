#Aula07 Exercicio Curso em Vídeo Python
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela
#pode comprar.
#Considere
#US$1,00=R$3.27 (atualmente 5,42 em 17/02/2021)
dinheiro = float(input('Quantidade de dinheiro em real R$ '))
dolar = dinheiro/5.42
euro = dinheiro/6.52
print('Você pode comprar US${:.2f} dólar(es).'.format(dolar))
print('Você pode comprar {:.2f} € euro(s).'.format(euro))
