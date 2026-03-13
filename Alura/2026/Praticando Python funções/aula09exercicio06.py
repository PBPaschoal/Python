#Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.
#Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
#Exemplo de entrada:
#Digite os números separados por espaço: 1 2 3 4 5 6
#Saída esperada:
#Números pares: 2 4 6 

numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 