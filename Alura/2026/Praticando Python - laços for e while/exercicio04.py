#Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. 
#Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.
#clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
#Ajude Ana a decidir entre usar um laço for ou while. Escreva o programa usando o laço que você acredita ser mais adequado para essa tarefa e explique por que escolheu esse laço.
clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
for cliente in clientes:
    """
    O laço for é mais adequado nesse caso, pois sabemos o número exato de elementos na lista (5 nomes). 
    Com o laço for, iremos percorrer todos os itens de maneira clara e direta, sem precisar gerenciar manualmente um contador ou condição de parada.
    """
    print(cliente)
