# Do básico ao avançado!
# Exercício 10
# Exibir apenas números pares de 1 a 50
# - Use for e condiçã.
# - Dica: ou use range (2, 51, 2).

# Primeira versão
print('Primeira versão:')
for i in range(2, 51, 2):
    print(i)

# Segunda versão
print('Segunda versão')
for i in range(2, 51):
    if i % 2 == 0:
        print(i)