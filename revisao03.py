# -- coding: utf-8 --

"""
Comando else
É executado caso a condição do comando if não seja atendida
Exemplo:
"""

x = 1
y = 2

if x > y:
	print("x maior que y")

else:
	print("y maior que x")

#Também podemos fazer assim:

a = -2
b = 4

if b > a:
	if b > 0:
		print("b é maior que a\nb é positivo")
	else:
		print("b não é maior que a nem positivo")
else:
	print("b menor que a")

"""
Comando elif
Caso haja necessidade de mais condições entre o if e o else

Sintaxe

if condição:
	execute_esta_linha
elif condição:
	execute_esta_linha
else:
	execute_esta_linha
"""

if x == y:
	print("Numeros iguais")
elif y > x:
	print("y maior que x") #Executado, pois é a primeira opção verdadeira
else:
	print("Numeros diferentes") #Não é executado, pois não chegou até ele. 
	