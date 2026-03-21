#Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
#Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
#Exemplo de entrada:
#Digite uma palavra: tecnologia 
#Saída esperada:
#Essa palavra tem 10 caracteres. 

def contagem_de_caracteres(palavra):
    palavra = len(palavra)
    return palavra

palavra = input('Digite uma palavra: ')
resultado = contagem_de_caracteres(palavra)
print(f'Essa palavra tem {resultado} caracteres.')