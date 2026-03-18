#Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. 
#Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.
#
#Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.
#
#Exemplo de entrada:
#
#Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais
#
#Saída esperada:
#
#Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais 
#
#Se nenhum palavra longa for encontrada:
#
#Nenhuma palavra longa foi encontrada no texto.  

texto = input("Digite um texto: ")
 
palavras_longas = []
 
for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longas.append(palavra)
 
if palavras_longas:
    print("Palavras longas encontradas:")
    for palavra in palavras_longas:
        print(palavra)
else:
    print("Nenhuma palavra longa foi encontrada no texto.")