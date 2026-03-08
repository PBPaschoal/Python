#Refaça o desafio 009 (do curso em vídeo - aqui eu numerei diferente), 
#mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero_escolhido = int(input('Digite um número para visualizar a tabuada: '))
for i in range(1, 11):
    resultado = numero_escolhido * i
    print(f'{numero_escolhido} * {i} = {resultado}')