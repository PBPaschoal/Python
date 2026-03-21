# Do básico ao avançado!
# Exercício 08
# Somar todos os números de 1 até N
# • 	Use laço ou fórmula matemática.
# • 	Dica: acumulador dentro do loop.
numero = int(input('Digite um número: '))
resultado = 1
for i in range(1, numero + 1):
    #print(f'{resultado} + {i}')
    resultado += i
    
print(resultado)