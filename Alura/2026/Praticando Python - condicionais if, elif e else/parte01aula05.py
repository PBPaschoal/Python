#Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. 
#No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.
#Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.
#Saída esperada:
#Informe os dias para a atividade A: 5
#Informe os dias para a atividade B: -8
#Informe os dias para a atividade C: 10
#Erro: Os dias não podem ser negativos.
diasA = int(input('Informe os dias para a atividade A: '))
diasB = int(input('Informe os dias para a atividade B: '))
diasC = int(input('Informe os dias para a atividade C: '))
if (diasA >= 0 and diasB >= 0 and diasC >= 0):
    tempo_total = diasA + diasB + diasC
    print(f'O tempo total do projeto é de {tempo_total} dias.')
else:
    print('Os dias não podem ser negativos.')