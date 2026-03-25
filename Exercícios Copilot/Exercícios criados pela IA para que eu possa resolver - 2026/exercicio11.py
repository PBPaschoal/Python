# Do básico ao avançado!
# Exercício 11
# Calcular a média de uma lista de números
# Some todos e divida pela quantidade.
# Dica: len(lista) ajuda.

# Primeira versão
print('Primeira versão:')
notas = [5, 9, 10, 3]
soma = 0
for i in range(1, len(notas)):
    soma = sum(notas)
    resultado = soma / len(notas)

print(f'Resultado: {resultado:.2f}\n')

# Segunda versão
def calculoSoma(notas2):
    soma = 0
    for i in range(1, len(notas2)):
        soma = sum(notas2)
        return soma / len(notas2)

print('Segunda versão:')
notas2 = [3, 7, 9, 2, 1, 6, 5]
resultado = calculoSoma(notas2)
print(f'Resultado: {resultado:.2f}\n')