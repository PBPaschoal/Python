#Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
#Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
#Saída esperada:
#Digite a temperatura atual: 30
#Alerta! Temperatura acima do limite permitido.
temperatura_atual = int(input('Digite a temperatura atual: '))
if temperatura_atual > 25:
    print('Alerta! Temperatura acima do limite permitido.')
else:
    print('Temperatura dentro do limite seguro.')