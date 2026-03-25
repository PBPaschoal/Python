# Do básico ao avançado!
# Exercício 20
# Simular um caixa eletrônico que dá troco em notas
# - Receba um valor e divida em notas de 100, 50, 20, 10, 5, 2, 1.
# - Dica: use divisão inteira (//) e resto (%)
valor = int(input("Digite o valor: "))

notas_100 = valor // 100
valor = valor % 100

notas_50 = valor // 50
valor = valor % 50

notas_20 = valor // 20
valor = valor % 20

notas_10 = valor // 10
valor = valor % 10

notas_5 = valor // 5
valor = valor % 5

notas_2 = valor // 2
valor = valor % 2

notas_1 = valor

print("Notas de 100:", notas_100)
print("Notas de 50:", notas_50)
print("Notas de 20:", notas_20)
print("Notas de 10:", notas_10)
print("Notas de 5:", notas_5)
print("Notas de 2:", notas_2)
print("Notas de 1:", notas_1)