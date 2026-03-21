# Do básico ao avançado!
# Exercício 12
# Verificar se uma palavra é palíndromo
# - Compare a palavra com ela invertida.
# - Dica: palavra[::-1]

# Primeira versão
palavra = input('Digite uma palavra: ')
invertida = palavra[::-1]
print(f'A palavra "{palavra}" invertida é: "{invertida}"')

# Segunda versão
palavra = input('Digite uma palavra: ').lower()
invertida = palavra[::-1]
if palavra == invertida:
    print(f'A palavra digitada é palíndromo, pois é igual a palavra invertida!\nPalavra "{palavra}" invertida é: "{invertida}"')
else:
    print(f'A palavra digitada não é palíndromo, pois é diferente da palavra invertida!\nPalavra "{palavra}" invertida é: "{invertida}" ')