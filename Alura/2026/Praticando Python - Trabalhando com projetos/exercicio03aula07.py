#Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. 
#Isso ajudará a analisar a estrutura das palavras utilizadas.
#
#Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
#
#Exemplo de entrada:
#
#Digite um texto: A linguagem Python é muito versátil.  
#
#Saída esperada:
#
#O texto contém 13 vogais. 
def contar_vogais(texto):
    vogais = 'aeiou'
    quantidade = 0
    for letra in texto.lower():
        if letra in vogais:
            quantidade += 1
    return quantidade

texto = input('Digite um texto: ')
print(f'O texto contém {contar_vogais(texto)} vogais.')