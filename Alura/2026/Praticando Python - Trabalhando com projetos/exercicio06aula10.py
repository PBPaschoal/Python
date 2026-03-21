#Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.
#
#Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:
#
#Pedra ganha de Tesoura (Pedra quebra Tesoura);
#Tesoura ganha de Papel (Tesoura corta Papel);
#Papel ganha de Pedra (Papel cobre Pedra);
#Se ambos escolherem a mesma opção, é um empate.
#Exemplo de entrada:
#
#Escolha: pedra, papel ou tesoura? papel  
#Saída esperada:
#
#Computador escolheu: pedra
#Você venceu! 
#
#Caso o computador vença:
#
#Computador escolheu: tesoura  
#Você perdeu!  
#Caso o computador escolha a mesma opção que você:
#Computador escolheu: papel 
#Empate!

import random

def pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_do_computador = random.choice(opcoes)
    escolha_do_usuario = input('Escolha: pedra, papel ou tesoura? ').lower()

    if escolha_do_usuario not in opcoes:
        print('Escolha inválida!')
        return
    
    print(f'Computador escolheu: {escolha_do_computador}')

    if escolha_do_usuario == escolha_do_computador:
        print('Empate!')
    elif (
        (escolha_do_usuario == 'pedra' and escolha_do_computador == 'tesoura') or
        (escolha_do_usuario == 'papel' and escolha_do_computador == 'pedra') or
        (escolha_do_usuario == 'tesoura' and escolha_do_computador == 'papel')
    ):
        print('Você venceu!')
    else:
        print('Você perdeu!')

pedra_papel_tesoura()