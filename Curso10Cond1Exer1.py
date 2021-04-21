#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
print('Computador pensando...')
import random
computador = random.randrange(0, 5)
numero = int(input('Pronto! De 0 à 5 qual número o computador escolheu? '))
if numero == computador:
    print('VOCÊ VENCEU!!!!')
else:
    print('ERROU! O COMPUTADOR VENCEU!!!')
print('Numero escolhido pelo computador: ', computador)



