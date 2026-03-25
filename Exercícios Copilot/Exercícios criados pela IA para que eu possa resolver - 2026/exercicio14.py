# Do básico ao avançado!
# Exercício 14
# Gerar os 10 primeiros números da sequência de Fibonacci
# - Cada número é a soma dos dois anteriores.
# - Dica: comece com [0,1].

# Começamos com os dois primeiros números da base
fibonacci = [0, 1]

# Queremos os 10 primeiros, já temos 2, então faltam 8
for i in range(8):
    # Pegamos o último número da lista: fibonacci[-1]
    # Pegamos o penúltimo número da lista: fibonacci[-2]
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    
    # Adicionamos o resultado no final da lista
    fibonacci.append(proximo_numero)

# Mostra o resultado final
print(f"Os 10 primeiros números: {fibonacci}")