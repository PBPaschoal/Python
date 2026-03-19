# Do básico ao avançado!
# Exercício 01
# - Imprimir números de 1 a 10
# Pense em como usar um laço de repetição (for ou while).
# Dica: o range() pode te ajudar.

# Primeira versão:
print('For')
for numero in range(1, 11):
    print(numero)

print('While')
contagem = 1

# Segunda versão:
while contagem <= 10:
    print(contagem)
    contagem += 1

print('While 02')
while True:
    if contagem <= 10:
        print(contagem)
        contagem += 1
    else:
        break