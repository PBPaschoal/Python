#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
valor = int(input('Informe um número: '))
if valor % 2 == 0:
    print(f'{valor} é par!')
else:
    print(f'{valor} é ímpar!')

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.
idade = int(input("Digite sua idade: "))
if 0 < idade <= 12:
    print("Criança")
elif 12 < idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else: 
    print("Valor inválido!")

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
usuario = input('Informe o usuário: ')
senha = int(input('Informe a senha: '))
if usuario == 'pbpaschoal' and senha == 8484:
    print('Usuário e senha corretos!')
else:
    print('Usuário ou senha invalida')

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.
x = int(input('Informe o valor de x: '))
y = int(input('Informe o valor de y: '))
if x > 0 and y > 0:
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quadrante')
elif x < 0 and y < 0:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadrante')
else:
    print('O ponto está sobre um eixo ou na origem')