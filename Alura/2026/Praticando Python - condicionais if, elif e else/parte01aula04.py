#Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
#Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
#Saída esperada:
#Digite a quantidade de maçãs vendidas: 15
#Digite a quantidade de bananas vendidas: 3
#As maçãs tiveram mais vendas.

quantidadeMacas = int(input('Digite a quantidade de maçãs vendidas: '))
quantidadeBananas = int(input('Digite a quantidade de bananas vendidas: '))
if quantidadeMacas > quantidadeBananas:
    print('As maças tiveram mais vendas')
elif quantidadeMacas < quantidadeBananas:
    print('As bananas tiveram mais vendas')
else:
    print('As vendas foram iguais.')