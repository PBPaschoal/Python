# Do básico ao avançado!
# Exercício 08
# - Verificar se um número é positivo, negativo ou zero
# - Use if, elif, else.
# - Dica: três condições diferentes.
numero = int(input('Digite um número: '))
if numero > 0:
    print(f'{numero} é positivo!')
elif numero < 0:
    print(f'{numero} é negativo!')
else:
    print(f'Você digitou {numero}')