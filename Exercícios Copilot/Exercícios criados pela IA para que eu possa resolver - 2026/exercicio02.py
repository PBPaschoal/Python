# Do básico ao avançado!
# Exercício 02
# - Somar dois números digitados pelo usuário
# - Use input() para receber valores.
# - Dica: lembre-se de converter para int ou float.

# Primeira versão:
primeiroValor = int(input('Digite um valor inteiro: '))
segundoValor = int(input('Digite outro valor inteiro: '))
soma = primeiroValor + segundoValor
print(f'{primeiroValor} + {segundoValor} = {soma}')

# Segunda versão:
def calcularSoma(a, b):
    soma = a + b
    return soma

valor01 = int(input('Digite um valor inteiro: '))
valor02 = int(input('Digite outro valor inteiro: '))
print(f'{valor01} + {valor02} = {calcularSoma(valor01, valor02)}')
# Podemos fazer da mesma forma usando float e adicionar casas decimais nos resultados.