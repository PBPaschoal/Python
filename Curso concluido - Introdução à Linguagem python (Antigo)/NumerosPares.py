#Rio de Janeiro - Dia 08/07/2021
#Faça um programa que mostre os números pares entre 1 e 100, inclusive.
#Entrada:
#Neste problema extremamente simples de repetição não há entrada.
#Saída:
#Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

for num in range(1,101): # testa se num é par
    if num %2 ==0: # se sim, mostra num
        print(num) # o print já pula uma linha a cada iteração