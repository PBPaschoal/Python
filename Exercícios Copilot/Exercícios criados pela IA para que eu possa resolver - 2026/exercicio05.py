# Do básico ao avançado!
# Exercício 05
#- Tabuada de um número
# - Use um laço para multiplicar de 1 a 10.
# - Dica: for i in range(1,11).

valor = int(input('Digite um número: '))
print(f'A tabuada de {valor} é:')
for numero in range(1, 11):
    resultado = valor * numero
    print(f'{valor} * {numero} = {resultado}')