# Do básico ao avançado!
# Exercício 13
# - Contar quantas vogais existem em uma palavra
# - Percorra cada letra e verifique se está em "aeiou".
# - Dica: use in.
vogais = 'aeiou'
contagem = 0
palavra = input('Digite uma palavra: ').lower()
for letra in palavra:
    if letra in vogais:
        contagem += 1

print(f'Total: {contagem}')