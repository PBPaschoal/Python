# Do básico ao avançado!
# Exercício 15
# Verificar se um número é primo
# - Teste divisões até raiz quadrada dele.
# - Dica: se só divide por 1 e ele mesmo, é primo.

import math

def eh_primo(n):
    # Números menores ou iguais a 1 não são primos
    if n <= 1:
        return False
    
    # O número 2 é o único par que é primo
    if n == 2:
        return True

    # Se for par e maior que 2, já sabemos que não é primo
    if n % 2 == 0:
        return False

    # A REGRA DA RAIZ QUADRADA:
    # Testamos apenas os números ímpares de 3 até a raiz quadrada de n
    limite = int(math.sqrt(n)) + 1
    
    for i in range(3, limite, 2):
        if n % i == 0:
            # Se o resto da divisão for 0, encontramos um divisor!
            return False
            
    # Se o laço terminar sem encontrar divisores, o número é primo
    return True

# --- Testando o código ---
numero = int(input("Digite um número para testar: "))

if eh_primo(numero):
    print(f"O número {numero} é PRIMO!")
else:
    print(f"O número {numero} NÃO é primo.")