#Aula07 Exercicio Curso em Vídeo Python
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salarioatual = float(input('Salario do funcionário R$'))
novosalario = salarioatual + (salarioatual * 15 / 100)
print('Novo salario com aumento de 15% = R${:.2f}'.format(novosalario))
