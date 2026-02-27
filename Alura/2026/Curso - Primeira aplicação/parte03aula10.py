print("""#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.""")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nomes = ['Bruno', 'Bruna', 'Pandora', 'Alice']
lista_anos = [1992, 2026]

print('\n#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.')
lista_cidades = ['Rio de Janeiro', 'Saquarema', 'Bacaxa']
cidade = 0
for cidade in lista_cidades:
    print(cidade)

print('\n#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.')
numero_impar = 0
for numero in range(1, 11):
    if numero % 2 != 0:
        numero_impar = numero_impar + numero

print("Soma dos ímpares:", numero_impar)

print('\n#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.')
for numero in range(10, 0, -1):
    print(numero)

print('\n#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.')
numero = int(input('Informe um número: '))
for i in range(1, 11):
    tabuada = numero * i
    print(f'{numero} x {i} = {tabuada}')

print('\n#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.')
lista_numeros_aleatorios = [3, 55, 91, 100, 101]
try:
    soma = 0
    for i in lista_numeros_aleatorios:
        soma += i
    print("Soma:", soma)
except Exception as e:
    print("Erro:", e)

print('\n7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.')
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")