# Do básico ao avançado!
# Exercício 03
# Verificar se um número é par ou ímpar
# • 	Use o operador  (resto da divisão).
# • 	Dica: se , é par.

# Primeira versão
def ParOuImpar(numero):
    if numero % 2 == 0:
        print(f'{numero} é par!')
    else:
        print(f'{numero} é ímpar!')
    return numero

numero = int(input('Digite um número: '))
ParOuImpar(numero)

# Segunda versão
valor = int(input('Digite um número: '))
if valor % 2 == 0:
    print(f'{valor} é par!')
else:
    print(f'{valor} é ímpar!')