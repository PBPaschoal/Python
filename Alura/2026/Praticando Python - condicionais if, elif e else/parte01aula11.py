#Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:
#Até 100 km: R$ 10,00
#Entre 100 km e 200 km: R$ 20,00
#Acima de 200 km: R$ 30,00
#Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
#Saída esperada:
#Digite a distância percorrida (em km): 250
#Valor do pedágio: R$ 30,00
texto = 'Valor do pedágio: R$'
distancia = int(input('Digite a distância percorrida (em km): '))
if distancia <= 100:
    print(f'{texto} 10,00')
elif distancia <= 200:
    print(f'{texto} 20,00')
else:
    print(f'{texto} 30,00')

