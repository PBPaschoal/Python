# Do básico ao avançado!
# Exercício 07
# - Calcular fatorial de um número
# - Multiplique todos os números de 1 até ele.
# - Dica: pense em laço acumulando o resultado.

# Primeira versão
numero = 5
resultado = 1

for i in range(1, numero + 1):
    resultado *= i

print(resultado)

# Segunda versão
numero = 5
resultado = 1

while numero > 0:
    resultado *= numero
    numero -= 1

print(resultado)