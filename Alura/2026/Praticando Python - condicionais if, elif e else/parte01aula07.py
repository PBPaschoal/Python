#Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. 
##O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. 
#Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2)
#Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
#Saída esperada:
#Digite seu peso (kg): 75
#Digite sua altura (m): 1.68
#Seu IMC é: 26.57
#Você está acima do peso.
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está com peso normal')
else:
    print('Você está acima do peso.')